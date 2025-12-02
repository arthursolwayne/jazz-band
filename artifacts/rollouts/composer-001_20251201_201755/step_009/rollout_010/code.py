
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (38, 0.375, 0.125),  # Snare on 2
    (42, 0.375, 0.125),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.125),  # Hihat on 3
    (38, 1.125, 0.125),  # Snare on 4
    (42, 1.125, 0.125)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass - walking line: F2, G2, Ab2, A2 (MIDI 38, 43, 44, 45)
bass_notes = [
    (38, 1.5, 0.375),  # F2 on 1
    (43, 1.875, 0.375),  # G2 on 2
    (44, 2.25, 0.375),  # Ab2 on 3
    (45, 2.625, 0.375)   # A2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> MIDI 53, 56, 60, 61
piano_notes = [
    (53, 1.5, 0.375),
    (56, 1.5, 0.375),
    (60, 1.5, 0.375),
    (61, 1.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - motif: F, Ab, G, F (MIDI 53, 56, 55, 53)
sax_notes = [
    (53, 1.5, 0.375),
    (56, 1.875, 0.375),
    (55, 2.25, 0.375),
    (53, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass - walking line: Bb2, B2, C2, Db2 (MIDI 42, 45, 46, 47)
bass_notes = [
    (42, 3.0, 0.375),  # Bb2 on 1
    (45, 3.375, 0.375),  # B2 on 2
    (46, 3.75, 0.375),  # C2 on 3
    (47, 4.125, 0.375)   # Db2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - open voicings: Bbmaj7 (Bb, D, F, Ab) -> MIDI 50, 55, 57, 56
piano_notes = [
    (50, 3.0, 0.375),
    (55, 3.0, 0.375),
    (57, 3.0, 0.375),
    (56, 3.0, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - motif: Bb, D, C, Bb (MIDI 50, 55, 52, 50)
sax_notes = [
    (50, 3.0, 0.375),
    (55, 3.375, 0.375),
    (52, 3.75, 0.375),
    (50, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass - walking line: Eb2, F2, G2, Ab2 (MIDI 47, 48, 49, 50)
bass_notes = [
    (47, 4.5, 0.375),  # Eb2 on 1
    (48, 4.875, 0.375),  # F2 on 2
    (49, 5.25, 0.375),  # G2 on 3
    (50, 5.625, 0.375)   # Ab2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - open voicings: Eb7sus4 (Eb, G, Bb, D) -> MIDI 47, 50, 52, 55
piano_notes = [
    (47, 4.5, 0.375),
    (50, 4.5, 0.375),
    (52, 4.5, 0.375),
    (55, 4.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - motif: Eb, G, F, Eb (MIDI 47, 50, 53, 47)
sax_notes = [
    (47, 4.5, 0.375),
    (50, 4.875, 0.375),
    (53, 5.25, 0.375),
    (47, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums - same pattern as bar 1
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
