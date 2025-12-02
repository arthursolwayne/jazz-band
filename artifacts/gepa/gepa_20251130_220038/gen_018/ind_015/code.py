
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
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 0.75), (38, 1.125), (42, 0.75),
    (36, 1.5), (38, 1.875), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 2.75), (46, 3.125), (44, 3.5), (43, 3.875),
    (45, 4.0), (46, 4.375), (44, 4.75), (43, 5.125),
    (45, 5.25), (46, 5.625), (44, 6.0), (43, 6.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 2.0), (62, 2.0), (64, 2.0), (67, 2.0),
    # Bar 3
    (60, 3.0), (63, 3.0), (65, 3.0), (68, 3.0),
    # Bar 4
    (59, 4.0), (62, 4.0), (64, 4.0), (67, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start it, leave it hanging. Come back and finish it.
# F7 -> G7 -> A7 -> Bb7
sax_notes = [
    (63, 1.5), (65, 1.625), (67, 1.875), (69, 2.0),
    (63, 2.75), (65, 2.875), (67, 3.0), (69, 3.125),
    (63, 3.75), (65, 3.875), (67, 4.0), (69, 4.125),
    (63, 4.75), (65, 4.875), (67, 5.0), (69, 5.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
