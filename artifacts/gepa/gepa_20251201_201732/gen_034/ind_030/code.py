
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
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38), F2 (40), G2 (43), D2 (38) - chromatic approach on F2
    (38, 1.5, 0.375),
    (40, 1.875, 0.375),
    (43, 2.25, 0.375),
    (38, 2.625, 0.375),
    # Bar 3: G2 (43), A2 (45), Bb2 (42), G2 (43) - chromatic approach on A2
    (43, 3.0, 0.375),
    (45, 3.375, 0.375),
    (42, 3.75, 0.375),
    (43, 4.125, 0.375),
    # Bar 4: D2 (38), F2 (40), G2 (43), D2 (38) - chromatic approach on F2
    (38, 4.5, 0.375),
    (40, 4.875, 0.375),
    (43, 5.25, 0.375),
    (38, 5.625, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes_bar2 = [(65, 1.5, 0.1875), (68, 1.5, 0.1875), (62, 1.5, 0.1875), (67, 1.5, 0.1875)]
# Bar 3: G7 (B, D, G, F)
piano_notes_bar3 = [(71, 3.0, 0.1875), (68, 3.0, 0.1875), (67, 3.0, 0.1875), (65, 3.0, 0.1875)]
# Bar 4: Cm7 (E, G, C, F)
piano_notes_bar4 = [(64, 4.5, 0.1875), (67, 4.5, 0.1875), (60, 4.5, 0.1875), (65, 4.5, 0.1875)]
for note, start, dur in piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (42, 1.5, 0.1875),  # Kick and hihat on 1
    (38, 1.875, 0.375), (42, 1.875, 0.1875),  # Snare and hihat on 2
    (36, 2.25, 0.375), (42, 2.25, 0.1875),  # Kick and hihat on 3
    (38, 2.625, 0.375), (42, 2.625, 0.1875),  # Snare and hihat on 4
    (36, 3.0, 0.375), (42, 3.0, 0.1875),  # Kick and hihat on 1
    (38, 3.375, 0.375), (42, 3.375, 0.1875),  # Snare and hihat on 2
    (36, 3.75, 0.375), (42, 3.75, 0.1875),  # Kick and hihat on 3
    (38, 4.125, 0.375), (42, 4.125, 0.1875),  # Snare and hihat on 4
    (36, 4.5, 0.375), (42, 4.5, 0.1875),  # Kick and hihat on 1
    (38, 4.875, 0.375), (42, 4.875, 0.1875),  # Snare and hihat on 2
    (36, 5.25, 0.375), (42, 5.25, 0.1875),  # Kick and hihat on 3
    (38, 5.625, 0.375), (42, 5.625, 0.1875)   # Snare and hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F4 (65), Eb4 (63), D4 (62) - played on 1.5, 1.875, 2.25, 2.625
# Then repeat on 3.0, 3.375, 3.75, 4.125, but leave the last note hanging
sax_notes = [
    (62, 1.5, 0.1875),
    (65, 1.875, 0.1875),
    (63, 2.25, 0.1875),
    (62, 2.625, 0.1875),
    (62, 3.0, 0.1875),
    (65, 3.375, 0.1875),
    (63, 3.75, 0.1875),
    (62, 4.125, 0.1875),
    (62, 4.5, 0.25)  # Hang the last note
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
