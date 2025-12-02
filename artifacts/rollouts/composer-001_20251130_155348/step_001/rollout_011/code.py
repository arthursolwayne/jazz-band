
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
    (36, 0.0, 0.375), # Kick on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (36, 0.75, 0.375), # Kick on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (42, 0.9375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375), # D
    (61, 1.875, 0.375), # C
    (63, 2.25, 0.375), # Eb
    (64, 2.625, 0.375), # F
    (62, 3.0, 0.375), # D
    (61, 3.375, 0.375), # C
    (63, 3.75, 0.375), # Eb
    (64, 4.125, 0.375), # F
    (62, 4.5, 0.375), # D
    (61, 4.875, 0.375), # C
    (63, 5.25, 0.375), # Eb
    (64, 5.625, 0.375) # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375), # D
    (67, 1.5, 0.375), # G
    (69, 1.5, 0.375), # Bb
    (64, 1.5, 0.375), # F
    (62, 1.875, 0.375), # D
    (67, 1.875, 0.375), # G
    (69, 1.875, 0.375), # Bb
    (64, 1.875, 0.375), # F
    # Bar 3
    (62, 2.25, 0.375), # D
    (67, 2.25, 0.375), # G
    (69, 2.25, 0.375), # Bb
    (64, 2.25, 0.375), # F
    (62, 2.625, 0.375), # D
    (67, 2.625, 0.375), # G
    (69, 2.625, 0.375), # Bb
    (64, 2.625, 0.375), # F
    # Bar 4
    (62, 3.0, 0.375), # D
    (67, 3.0, 0.375), # G
    (69, 3.0, 0.375), # Bb
    (64, 3.0, 0.375), # F
    (62, 3.375, 0.375), # D
    (67, 3.375, 0.375), # G
    (69, 3.375, 0.375), # Bb
    (64, 3.375, 0.375), # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375), # D
    (65, 1.875, 0.375), # F
    (62, 2.25, 0.375), # D
    (64, 2.625, 0.375), # F
    (62, 3.0, 0.375), # D
    (65, 3.375, 0.375), # F
    (62, 3.75, 0.375), # D
    (64, 4.125, 0.375), # F
    (62, 4.5, 0.375), # D
    (65, 4.875, 0.375), # F
    (62, 5.25, 0.375), # D
    (64, 5.625, 0.375) # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with the pattern
drum_notes = [
    (36, 1.5, 0.375), # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875), # Hihat on 1 & 2
    (42, 1.6875, 0.1875),
    (36, 2.25, 0.375), # Kick on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.25, 0.1875), # Hihat on 3 & 4
    (42, 2.4375, 0.1875),
    (36, 3.0, 0.375), # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875), # Hihat on 1 & 2
    (42, 3.1875, 0.1875),
    (36, 3.75, 0.375), # Kick on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 3.75, 0.1875), # Hihat on 3 & 4
    (42, 3.9375, 0.1875),
    (36, 4.5, 0.375), # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (36, 5.25, 0.375), # Kick on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.25, 0.1875), # Hihat on 3 & 4
    (42, 5.4375, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
