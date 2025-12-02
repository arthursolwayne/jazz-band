
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key (F major)
key = 'F'

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drums_program = pretty_midi.instrument_name_to_program('Drums')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [bass, piano, sax, drums]

# Note duration in seconds (60 / BPM = 0.375 seconds per beat)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar
time = 0.0

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]  # C2 kicks on beat 1 and 3
snare_notes = [38, 38]  # G2 snares on beat 2 and 4
hihat_notes = [42] * 8  # C3 hihat on every eighth note

# Kick on beat 1 and 3
for i in range(2):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=time + i * beat, end=time + i * beat + beat / 4)
    drums.notes.append(kick)

# Snare on beat 2 and 4
for i in range(2):
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=time + i * beat + beat / 2, end=time + i * beat + beat / 2 + beat / 4)
    drums.notes.append(snare)

# Hihat on every eighth note
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=hihat_notes[i], start=time + i * beat / 2, end=time + i * beat / 2 + beat / 8)
    drums.notes.append(hihat)

time += bar

# Bar 2: Bass (Marcus) - Walking line with chromatic approaches
# F major scale: F G A Bb C D E
# Walking bass line with chromatic passing tones

# Notes in F major (MIDI numbers)
f = 65
g = 67
a = 69
bb = 70
c = 72
d = 74
e = 76

# Walking bass line with chromatic passing
bass_notes = [
    f,  # F (beat 1)
    66, # F#
    g,  # G (beat 2)
    71, # Bb
    a,  # A (beat 3)
    73, # B
    bb, # Bb (beat 4)
    75  # B
]

# Add notes to bass
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + i * beat / 2, end=time + i * beat / 2 + beat / 4)
    bass.notes.append(note)

time += bar

# Bar 3: Piano (Diane) - 7th chords on 2 and 4
# F7 = F A C Eb
# Bb7 = Bb D F Ab
# D7 = D F# A C
# E7 = E G# B D

# Chord on beat 2 and 4
# F7 on beat 2
f7_notes = [65, 69, 72, 70]  # F A C Eb
# Bb7 on beat 4
bb7_notes = [70, 74, 72, 68]  # Bb D F Ab

# Add notes to piano
for i, chord in enumerate([f7_notes, bb7_notes]):
    for note in chord:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time + i * beat + beat / 2, end=time + i * beat + beat / 2 + beat / 2)
        piano.notes.append(piano_note)

time += bar

# Bar 4: Tenor Sax (You) - Melody with space
# Start with a motif: F - Bb - Eb - A (rest) - F - Bb - G (rest) - F
# Motif: F (beat 1), Bb (beat 2), Eb (beat 3), A (beat 4), then rest, then F (beat 1), Bb (beat 2), G (beat 3), rest on beat 4

# Note durations (quarter, quarter, quarter, quarter)
sax_notes = [
    (65, beat),  # F
    (70, beat),  # Bb
    (69, beat),  # Eb
    (72, beat),  # A
    (0, beat),   # Rest
    (65, beat),  # F
    (70, beat),  # Bb
    (67, beat),  # G
    (0, beat)    # Rest
]

# Add notes to sax
for i, (pitch, duration) in enumerate(sax_notes):
    if pitch == 0:
        continue  # Skip rests
    start_time = time + i * beat / 2
    sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + duration)
    sax.notes.append(sax_note)

# Save the MIDI file
pm.write("jazz_intro_wayne.mid")
