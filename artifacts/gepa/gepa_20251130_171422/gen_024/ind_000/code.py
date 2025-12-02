
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 1.0),   # Kick on 1
    (38, 0.5, 1.0),   # Snare on 2
    (42, 0.0, 1.0),   # Hihat on 1
    (42, 0.25, 1.0),  # Hihat on 2
    (42, 0.5, 1.0),   # Hihat on 3
    (42, 0.75, 1.0),  # Hihat on 4
    (36, 1.0, 1.0),   # Kick on 3
    (38, 1.5, 1.0),   # Snare on 4
    (42, 1.0, 1.0),   # Hihat on 3
    (42, 1.25, 1.0),  # Hihat on 4
    (42, 1.5, 1.0)    # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (64, 1.5, 0.5),   # F (root)
    (65, 2.0, 0.5),   # F# chromatic
    (65, 2.5, 0.5),   # F# again (bass line tension)
    (66, 3.0, 0.5),   # G
    (68, 3.5, 0.5),   # A
    (69, 4.0, 0.5),   # A#
    (70, 4.5, 0.5),   # B
    (69, 5.0, 0.5),   # A# again (tension before resolution)
    (67, 5.5, 0.5),   # Bb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 2.0, 0.25),  # D7 (D, F#, A, C)
    (64, 2.0, 0.25),
    (67, 2.0, 0.25),
    (69, 2.0, 0.25),
    (62, 4.0, 0.25),  # D7 again
    (64, 4.0, 0.25),
    (67, 4.0, 0.25),
    (69, 4.0, 0.25),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante on sax: sparse, emotional motif
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

sax_notes = [
    (66, 1.5, 0.5),   # A
    (68, 2.0, 0.5),   # B
    (69, 2.5, 0.5),   # B#
    (70, 3.0, 0.5),   # C
    (67, 3.5, 0.5),   # Bb
    (68, 4.0, 0.5),   # B
    (69, 4.5, 0.5),   # B#
    (70, 5.0, 0.5),   # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
