
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (65, 2.25),  # D, Eb, E, F
    (67, 2.5), (68, 2.75), (69, 3.0), (70, 3.25),  # G, G#, A, Bb
    (72, 3.5), (73, 3.75), (74, 4.0), (75, 4.25),  # B, C, C#, D
    (77, 4.5), (78, 4.75), (79, 5.0), (80, 5.25)   # D#, E, F, F#
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 2.0), (71, 2.0), (74, 2.0), (76, 2.0),  # G7 (G, B, D, F)
    # Bar 3
    (69, 3.0), (73, 3.0), (76, 3.0), (78, 3.0),  # A7 (A, C#, E, G)
    # Bar 4
    (72, 4.0), (76, 4.0), (79, 4.0), (81, 4.0)   # B7 (B, D#, F#, A)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), E (64), G (67), D (62)
# Bar 2: D (62) at 1.5s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6))
# Bar 2: E (64) at 1.75s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.85))
# Bar 3: G (67) at 3.0s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1))
# Bar 4: D (62) at 4.5s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
