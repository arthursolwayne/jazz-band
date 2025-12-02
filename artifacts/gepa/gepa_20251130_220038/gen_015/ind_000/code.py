
import pretty_midi

# Initialize the MIDI file with 160 BPM (4/4 time, 6 seconds for 4 bars)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Time per bar (6 seconds total for 4 bars)
bar_length = 1.5  # seconds per bar

# BAR 1: DRUMS ALONE (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (kick, 0.0), (snare, 0.75), (hihat, 0.0), (hihat, 0.375), (hihat, 0.75), (hihat, 1.125),
    (kick, 1.5), (snare, 1.5 + 0.75), (hihat, 1.5), (hihat, 1.5 + 0.375), (hihat, 1.5 + 0.75), (hihat, 1.5 + 1.125)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# BAR 2: FULL QUARTET (1.5 - 3.0s)

# SAX: Introduce the motif — simple, but with space and soul
# Dm7: D, F, A, C
# Motif: D (16th), F (eighth), A (eighth), C (quarter) — but start with D, then leave it hanging

sax_notes = [
    (62, 1.5, 0.25),  # D (16th)
    (65, 1.75, 0.5),  # F (eighth)
    (69, 2.25, 0.5),  # A (eighth)
    (67, 2.75, 0.5)   # C (quarter) — resolves the tension
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# BASS: Walking line in Dm
# Start on D (62), chromatic approach to F (65)
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Walking bass line: D → Eb → F → G (1st bar), then A → Bb → C → D (2nd bar)

bass_notes = [
    (62, 1.5, 0.25),  # D
    (63, 1.75, 0.25),  # Eb
    (65, 2.0, 0.25),   # F
    (67, 2.25, 0.25),  # G

    (69, 2.5, 0.25),   # A
    (70, 2.75, 0.25),  # Bb
    (72, 3.0, 0.25),   # C
    (62, 3.25, 0.25)   # D
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# PIANO: 7th chords, comp on 2 and 4 (beat 2 and 4 in bar 2)
# Dm7: D, F, A, C
# Play chord on beat 2 (1.75s) and beat 4 (2.5s) — spaced, no wash

piano_notes = [
    (62, 1.75, 0.25),  # D
    (65, 1.75, 0.25),  # F
    (69, 1.75, 0.25),  # A
    (67, 1.75, 0.25),  # C

    (62, 2.5, 0.25),   # D
    (65, 2.5, 0.25),   # F
    (69, 2.5, 0.25),   # A
    (67, 2.5, 0.25)    # C
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# BAR 3: FULL QUARTET (3.0 - 4.5s)

# SAX: Repeat the motif, but with subtle variation — maybe a half-step shift or a different rhythm
sax_notes = [
    (63, 3.0, 0.25),  # Eb (variation)
    (65, 3.25, 0.5),  # F
    (69, 3.75, 0.5),  # A
    (67, 4.25, 0.5)   # C
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# BASS: Walk another cycle
bass_notes = [
    (65, 3.0, 0.25),   # F
    (67, 3.25, 0.25),  # G
    (69, 3.5, 0.25),   # A
    (70, 3.75, 0.25),  # Bb

    (72, 4.0, 0.25),   # C
    (62, 4.25, 0.25),  # D
    (63, 4.5, 0.25),   # Eb
    (65, 4.75, 0.25)   # F
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# PIANO: Comp on 2 and 4 of bar 3 (beat 2 and 4)
# Play Dm7 again, spaced
piano_notes = [
    (62, 3.25, 0.25),  # D
    (65, 3.25, 0.25),  # F
    (69, 3.25, 0.25),  # A
    (67, 3.25, 0.25),  # C

    (62, 4.0, 0.25),   # D
    (65, 4.0, 0.25),   # F
    (69, 4.0, 0.25),   # A
    (67, 4.0, 0.25)    # C
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# BAR 4: FULL QUARTET (4.5 - 6.0s)

# SAX: End with the original motif, but with a hold on the last note
sax_notes = [
    (62, 4.5, 0.25),  # D (16th)
    (65, 4.75, 0.5),  # F (eighth)
    (69, 5.25, 0.5),  # A (eighth)
    (67, 5.75, 1.0)   # C (half note) — lingering beat
]
for pitch, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# BASS: Walk to the end, ending on D
bass_notes = [
    (69, 4.5, 0.25),   # A
    (70, 4.75, 0.25),  # Bb
    (72, 5.0, 0.25),   # C
    (62, 5.25, 0.25),  # D

    (63, 5.5, 0.25),   # Eb
    (65, 5.75, 0.25),  # F
    (67, 6.0, 0.25),   # G
    (62, 6.0, 0.25)    # D (hold)
]
for pitch, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# PIANO: Final comp on 2 and 4 (beat 2 and 4 of bar 4)
piano_notes = [
    (62, 4.75, 0.25),  # D
    (65, 4.75, 0.25),  # F
    (69, 4.75, 0.25),  # A
    (67, 4.75, 0.25),  # C

    (62, 5.5, 0.25),   # D
    (65, 5.5, 0.25),   # F
    (69, 5.5, 0.25),   # A
    (67, 5.5, 0.25)    # C
]
for pitch, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# DRUMS: Same pattern, but end on a snare on beat 4
drum_notes = [
    (kick, 4.5), (snare, 5.25), (hihat, 4.5), (hihat, 4.875), (hihat, 5.25), (hihat, 5.625),
    (kick, 6.0), (snare, 6.0 + 0.75), (hihat, 6.0), (hihat, 6.0 + 0.375), (hihat, 6.0 + 0.75), (hihat, 6.0 + 1.125)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
