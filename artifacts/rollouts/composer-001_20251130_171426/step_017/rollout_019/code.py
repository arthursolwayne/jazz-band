
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
    (36, 0.0, 1.5),   # Kick on beat 1
    (38, 0.75, 1.5),  # Snare on beat 2
    (42, 0.0, 1.5),   # Hihat on every eighth
    (42, 0.375, 1.5),
    (42, 0.75, 1.5),
    (42, 1.125, 1.5),
    (36, 1.5, 1.5),   # Kick on beat 3
    (38, 2.25, 1.5),  # Snare on beat 4
    (42, 1.5, 1.5),
    (42, 1.875, 1.5),
    (42, 2.25, 1.5),
    (42, 2.625, 1.5)
]

for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice. Dm7 = D F A C
# Bass line: D - Eb - F - G (chromatic approach to F), then D - Eb - F - G (again)
bass_notes = [
    (62, 1.5, 1.75),  # D
    (63, 1.75, 2.0),  # Eb
    (64, 2.0, 2.25),  # F
    (65, 2.25, 2.5),  # G
    (62, 2.5, 2.75),  # D
    (63, 2.75, 3.0),  # Eb
    (64, 3.0, 3.25),  # F
    (65, 3.25, 3.5),  # G
    (62, 3.5, 3.75),  # D
    (63, 3.75, 4.0),  # Eb
    (64, 4.0, 4.25),  # F
    (65, 4.25, 4.5),  # G
    (62, 4.5, 4.75),  # D
    (63, 4.75, 5.0),  # Eb
    (64, 5.0, 5.25),  # F
    (65, 5.25, 5.5),  # G
    (62, 5.5, 5.75),  # D
    (63, 5.75, 6.0)   # Eb
]

for note, start, end in bass_notes:
    nb = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(nb)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on beat 2 and 4 of each bar
# Bar 2: Dm7 on beat 2
# Bar 3: Dm7 on beat 2
# Bar 4: Dm7 on beat 2 and 4

piano_notes = [
    (62, 2.0, 2.5),  # D
    (65, 2.0, 2.5),  # F
    (69, 2.0, 2.5),  # A
    (72, 2.0, 2.5),  # C
    (62, 3.5, 4.0),  # D
    (65, 3.5, 4.0),  # F
    (69, 3.5, 4.0),  # A
    (72, 3.5, 4.0),  # C
    (62, 5.0, 5.5),  # D
    (65, 5.0, 5.5),  # F
    (69, 5.0, 5.5),  # A
    (72, 5.0, 5.5),  # C
    (62, 5.5, 6.0),  # D
    (65, 5.5, 6.0),  # F
    (69, 5.5, 6.0),  # A
    (72, 5.5, 6.0)   # C
]

for note, start, end in piano_notes:
    np = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(np)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - Eb - F - D (start), then D - G - Eb - D (finish)
# Bar 2: Start motif
# Bar 3: Leave it hanging
# Bar 4: Finish it

sax_notes = [
    (62, 1.5, 1.875),  # D
    (63, 1.875, 2.25), # Eb
    (64, 2.25, 2.625),# F
    (62, 2.625, 3.0),  # D
    (62, 3.5, 3.875),  # D
    (67, 3.875, 4.25), # G
    (63, 4.25, 4.625),# Eb
    (62, 4.625, 5.0),  # D
    (62, 5.5, 5.875),  # D
    (63, 5.875, 6.25), # Eb
    (64, 6.25, 6.625),# F
    (62, 6.625, 7.0)   # D
]

for note, start, end in sax_notes:
    ns = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(ns)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
