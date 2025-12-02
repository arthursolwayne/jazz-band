
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375))  # snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # hihat on every eighth

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (36, 1.5, 1.875), (37, 1.875, 2.25), (34, 2.25, 2.625), (35, 2.625, 3.0),
    (37, 3.0, 3.375), (38, 3.375, 3.75), (36, 3.75, 4.125), (39, 4.125, 4.5),
    (40, 4.5, 4.875), (39, 4.875, 5.25), (38, 5.25, 5.625), (37, 5.625, 6.0)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.5, 1.875), (61, 1.5, 1.875), (64, 1.5, 1.875), (62, 1.5, 1.875),
    # Bar 3
    (60, 3.0, 3.375), (62, 3.0, 3.375), (65, 3.0, 3.375), (63, 3.0, 3.375),
    # Bar 4
    (59, 4.5, 4.875), (61, 4.5, 4.875), (64, 4.5, 4.875), (62, 4.5, 4.875)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)) # kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999)) # kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)) # snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)) # snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25)) # kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=6.0))    # hihat on every eighth

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.75), (65, 1.75, 2.0), (62, 2.0, 2.25), (60, 2.25, 2.5),
    (62, 2.5, 2.75), (65, 2.75, 3.0), (62, 3.0, 3.25), (60, 3.25, 3.5),
    (62, 3.5, 3.75), (65, 3.75, 4.0), (62, 4.0, 4.25), (60, 4.25, 4.5),
    (62, 4.5, 4.75), (65, 4.75, 5.0), (62, 5.0, 5.25), (60, 5.25, 5.5),
    (62, 5.5, 5.75), (65, 5.75, 6.0)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
