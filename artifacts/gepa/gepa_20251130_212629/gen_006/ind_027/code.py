
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Set up time signature and key
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=160)]
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=1, time=0.0)]  # F major

# Define note durations and timing
beat = 0.375  # 160 BPM in 4/4 time
bar = 4 * beat  # 1.5 seconds per bar

# Bar 1: Drums only, tension and anticipation
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(0, 8):
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[i//2], start=i * beat, end=(i + 1) * beat)
        drums.notes.append(note)
    elif i % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=snare_notes[i//2], start=i * beat, end=(i + 1) * beat)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=i * beat, end=(i + 1) * beat)
    drums.notes.append(note)

pm.instruments.append(drums)

# Bar 2: Bass enters with walking line
bass_notes = [37, 40, 41, 43, 45, 47, 48, 49, 47, 45, 43, 41, 40, 37, 37, 39]  # Chromatic walking line
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=i * beat, end=(i + 1) * beat)
    bass.notes.append(note)

pm.instruments.append(bass)

# Bar 2-3: Piano enters with 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Rest on 1, chord on 2
    (63, 67, 70),  # F7 on beat 2
    (63, 67, 70, 69),  # F7 on beat 4
    # Bar 3: Rest on 1, chord on 2
    (63, 67, 70),  # F7 on beat 2
    (63, 67, 70, 69),  # F7 on beat 4
    # Bar 4: Rest on 1, chord on 2
    (63, 67, 70),  # F7 on beat 2
    (63, 67, 70, 69),  # F7 on beat 4
]

for i, chord in enumerate(piano_notes):
    for note in chord:
        start = (i + 2) * beat
        end = start + beat
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

pm.instruments.append(piano)

# Bar 2: Sax enters with short motif
# Motif: F (65), Ab (67), Bb (69), G (67), rest, F (65)
sax_notes = [
    (65, 0.375),  # F on beat 1
    (67, 0.375),  # Ab on beat 2
    (69, 0.375),  # Bb on beat 3
    (67, 0.375),  # G on beat 4
    (65, 0.75),   # F on beat 1 of next bar
]

for i, (pitch, duration) in enumerate(sax_notes):
    start = i * beat
    end = start + duration
    sax_note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(sax_note)

pm.instruments.append(sax)

# Write to MIDI file
pm.write('jazz_intro.mid')
