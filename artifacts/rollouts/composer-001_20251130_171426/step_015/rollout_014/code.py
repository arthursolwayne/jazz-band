
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1& 
    (42, 0.1875, 0.1875),  # Hihat on 2
    (38, 0.375, 0.375),  # Snare on 3
    (42, 0.375, 0.1875),  # Hihat on 3&
    (42, 0.5625, 0.1875),  # Hihat on 4
    (36, 0.75, 0.375),  # Kick on 2
    (42, 0.75, 0.1875),  # Hihat on 2&
    (42, 0.9375, 0.1875),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 4&
    (42, 1.3125, 0.1875)  # Hihat on 1
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: F, G#, Bb, C (start of melody)
sax_notes = [
    (84, 1.5, 0.375),  # F
    (87, 1.875, 0.375),  # G#
    (81, 2.25, 0.375),  # Bb
    (87, 2.625, 0.375)  # C
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bass line: walking in F
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375),  # G
    (62, 2.25, 0.375),  # Eb
    (64, 2.625, 0.375)  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (76, 1.875, 0.375),  # F7 (76=A, 75=G, 72=F, 74=G#, 77=Bb)
    (75, 1.875, 0.375),
    (72, 1.875, 0.375),
    (74, 1.875, 0.375),
    (77, 1.875, 0.375),
    (76, 2.625, 0.375),  # F7 again
    (75, 2.625, 0.375),
    (72, 2.625, 0.375),
    (74, 2.625, 0.375),
    (77, 2.625, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: repeat motif with slight variation
sax_notes = [
    (84, 3.0, 0.375),  # F
    (87, 3.375, 0.375),  # G#
    (81, 3.75, 0.375),  # Bb
    (87, 4.125, 0.375)  # C
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bass line: walking in F
bass_notes = [
    (64, 3.0, 0.375),  # F
    (65, 3.375, 0.375),  # G
    (62, 3.75, 0.375),  # Eb
    (64, 4.125, 0.375)  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4 again
piano_notes = [
    (76, 3.375, 0.375),  # F7
    (75, 3.375, 0.375),
    (72, 3.375, 0.375),
    (74, 3.375, 0.375),
    (77, 3.375, 0.375),
    (76, 4.125, 0.375),  # F7
    (75, 4.125, 0.375),
    (72, 4.125, 0.375),
    (74, 4.125, 0.375),
    (77, 4.125, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1&
    (42, 3.1875, 0.1875),  # Hihat on 2
    (38, 3.375, 0.375),  # Snare on 3
    (42, 3.375, 0.1875),  # Hihat on 3&
    (42, 3.5625, 0.1875),  # Hihat on 4
    (36, 3.75, 0.375),  # Kick on 2
    (42, 3.75, 0.1875),  # Hihat on 2&
    (42, 3.9375, 0.1875),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875),  # Hihat on 4&
    (42, 4.3125, 0.1875)  # Hihat on 1
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: repeat motif with a resolution on the 4th beat
sax_notes = [
    (84, 4.5, 0.375),  # F
    (87, 4.875, 0.375),  # G#
    (81, 5.25, 0.375),  # Bb
    (87, 5.625, 0.375)  # C (end on C)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bass line: walking in F
bass_notes = [
    (64, 4.5, 0.375),  # F
    (65, 4.875, 0.375),  # G
    (62, 5.25, 0.375),  # Eb
    (64, 5.625, 0.375)  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4 again
piano_notes = [
    (76, 4.875, 0.375),  # F7
    (75, 4.875, 0.375),
    (72, 4.875, 0.375),
    (74, 4.875, 0.375),
    (77, 4.875, 0.375),
    (76, 5.625, 0.375),  # F7
    (75, 5.625, 0.375),
    (72, 5.625, 0.375),
    (74, 5.625, 0.375),
    (77, 5.625, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1&
    (42, 4.6875, 0.1875),  # Hihat on 2
    (38, 4.875, 0.375),  # Snare on 3
    (42, 4.875, 0.1875),  # Hihat on 3&
    (42, 5.0625, 0.1875),  # Hihat on 4
    (36, 5.25, 0.375),  # Kick on 2
    (42, 5.25, 0.1875),  # Hihat on 2&
    (42, 5.4375, 0.1875),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875),  # Hihat on 4&
    (42, 5.8125, 0.1875)  # Hihat on 1
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
