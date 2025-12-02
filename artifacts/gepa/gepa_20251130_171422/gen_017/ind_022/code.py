
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Fill with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375),# Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.75, 0.1875),# Hihat on 3
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.125, 0.1875),# Hihat on 4
    (42, 1.5, 0.1875)  # Hihat on 4 end
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus plays walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 1.75), # D
    (63, 1.75, 2.0), # Eb
    (61, 2.0, 2.25), # C
    (62, 2.25, 2.5), # D
    (64, 2.5, 2.75), # E
    (65, 2.75, 3.0), # F
    (64, 3.0, 3.25), # E
    (63, 3.25, 3.5), # Eb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: Diane plays 7th chords on 2 and 4
piano_notes = [
    (67, 2.0, 2.25), # F7: F, A, C, Eb
    (69, 2.0, 2.25),
    (64, 2.0, 2.25),
    (62, 2.0, 2.25),
    (67, 3.0, 3.25),
    (69, 3.0, 3.25),
    (64, 3.0, 3.25),
    (62, 3.0, 3.25),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: Dante plays the motif
sax_notes = [
    (67, 1.5, 1.625), # F
    (69, 1.625, 1.75), # G
    (67, 1.75, 1.875), # F
    (71, 1.875, 2.0), # Bb
    (69, 2.0, 2.125), # G
    (67, 2.125, 2.25), # F
    (69, 2.25, 2.375), # G
    (71, 2.375, 2.5), # Bb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Marcus plays walking line with chromatic approaches
bass_notes = [
    (65, 3.0, 3.25), # F
    (66, 3.25, 3.5), # F#
    (64, 3.5, 3.75), # E
    (65, 3.75, 4.0), # F
    (67, 4.0, 4.25), # G
    (68, 4.25, 4.5), # G#
    (67, 4.5, 4.75), # G
    (66, 4.75, 5.0), # F#
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: Diane plays 7th chords on 2 and 4
piano_notes = [
    (67, 3.5, 3.75), # F7: F, A, C, Eb
    (69, 3.5, 3.75),
    (64, 3.5, 3.75),
    (62, 3.5, 3.75),
    (67, 4.5, 4.75),
    (69, 4.5, 4.75),
    (64, 4.5, 4.75),
    (62, 4.5, 4.75),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: Dante plays the motif again
sax_notes = [
    (67, 3.0, 3.125), # F
    (69, 3.125, 3.25), # G
    (67, 3.25, 3.375), # F
    (71, 3.375, 3.5), # Bb
    (69, 3.5, 3.625), # G
    (67, 3.625, 3.75), # F
    (69, 3.75, 3.875), # G
    (71, 3.875, 4.0), # Bb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 3.375),  # Kick on 1
    (42, 3.0, 3.1875), # Hihat on 1
    (38, 3.375, 3.375),# Snare on 2
    (42, 3.375, 3.1875),# Hihat on 2
    (36, 3.75, 3.375), # Kick on 3
    (42, 3.75, 3.1875),# Hihat on 3
    (38, 4.125, 3.375),# Snare on 4
    (42, 4.125, 3.1875),# Hihat on 4
    (42, 4.5, 3.1875)  # Hihat on 4 end
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: Marcus plays walking line with chromatic approaches
bass_notes = [
    (68, 4.5, 4.75), # G#
    (67, 4.75, 5.0), # G
    (68, 5.0, 5.25), # G#
    (67, 5.25, 5.5), # G
    (69, 5.5, 5.75), # A
    (71, 5.75, 6.0), # Bb
    (69, 6.0, 6.25), # A
    (67, 6.25, 6.5), # G
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: Diane plays 7th chords on 2 and 4
piano_notes = [
    (67, 4.75, 5.0), # F7: F, A, C, Eb
    (69, 4.75, 5.0),
    (64, 4.75, 5.0),
    (62, 4.75, 5.0),
    (67, 5.75, 6.0),
    (69, 5.75, 6.0),
    (64, 5.75, 6.0),
    (62, 5.75, 6.0),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: Dante plays the motif again, but finishes it
sax_notes = [
    (67, 4.5, 4.625), # F
    (69, 4.625, 4.75), # G
    (67, 4.75, 4.875), # F
    (71, 4.875, 5.0), # Bb
    (69, 5.0, 5.125), # G
    (67, 5.125, 5.25), # F
    (69, 5.25, 5.375), # G
    (71, 5.375, 5.5), # Bb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 4.875),  # Kick on 1
    (42, 4.5, 4.6875), # Hihat on 1
    (38, 4.875, 4.875),# Snare on 2
    (42, 4.875, 4.6875),# Hihat on 2
    (36, 5.25, 4.875), # Kick on 3
    (42, 5.25, 4.6875),# Hihat on 3
    (38, 5.625, 4.875),# Snare on 4
    (42, 5.625, 4.6875),# Hihat on 4
    (42, 6.0, 4.6875)  # Hihat on 4 end
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
