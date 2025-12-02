
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (61, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    # Bar 3
    (63, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4
    (63, 4.5, 0.375), (62, 4.875, 0.375), (60, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
# Dm7 = D F A C
piano_notes = [
    # Bar 2
    (50, 1.875, 0.375), (52, 1.875, 0.375), (55, 1.875, 0.375), (57, 1.875, 0.375),
    (50, 2.625, 0.375), (52, 2.625, 0.375), (55, 2.625, 0.375), (57, 2.625, 0.375),
    # Bar 3
    (50, 3.875, 0.375), (52, 3.875, 0.375), (55, 3.875, 0.375), (57, 3.875, 0.375),
    (50, 4.625, 0.375), (52, 4.625, 0.375), (55, 4.625, 0.375), (57, 4.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D F G A Bb C
# Motif: D F G (bar 2), A Bb (bar 3), D (bar 4)
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375), (64, 1.875, 0.375), (66, 2.25, 0.375),
    # Bar 3
    (69, 3.0, 0.375), (67, 3.375, 0.375),
    # Bar 4
    (62, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: Full bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.375)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.75)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 1.125)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)
    # Add all notes
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)
    drums.notes.append(hihat5)
    drums.notes.append(hihat6)
    drums.notes.append(hihat7)
    drums.notes.append(hihat8)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
