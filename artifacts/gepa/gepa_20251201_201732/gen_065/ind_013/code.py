
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

# Drums
drum_notes = [
    # Bar 1: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    (36, 0.0, 0.375), (38, 0.375, 0.75), (42, 0.0, 0.1875),
    (42, 0.1875, 0.375), (42, 0.375, 0.5625), (42, 0.5625, 0.75),
    (42, 0.75, 0.9375), (42, 0.9375, 1.125), (42, 1.125, 1.3125),
    (42, 1.3125, 1.5), (36, 1.5, 1.875), (38, 1.875, 2.25),
    (42, 1.5, 1.6875), (42, 1.6875, 1.875), (42, 1.875, 2.0625),
    (42, 2.0625, 2.25), (42, 2.25, 2.4375), (42, 2.4375, 2.625),
    (42, 2.625, 2.8125), (42, 2.8125, 3.0), (36, 3.0, 3.375),
    (38, 3.375, 3.75), (42, 3.0, 3.1875), (42, 3.1875, 3.375),
    (42, 3.375, 3.5625), (42, 3.5625, 3.75), (42, 3.75, 3.9375),
    (42, 3.9375, 4.125), (42, 4.125, 4.3125), (42, 4.3125, 4.5),
    (36, 4.5, 4.875), (38, 4.875, 5.25), (42, 4.5, 4.6875),
    (42, 4.6875, 4.875), (42, 4.875, 5.0625), (42, 5.0625, 5.25),
    (42, 5.25, 5.4375), (42, 5.4375, 5.625), (42, 5.625, 5.8125),
    (42, 5.8125, 6.0)
]

for note, start, end in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(note_obj)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (38)
bass_notes = [
    (38, 1.5, 1.875),  # D2
    (40, 1.875, 2.25),  # F2 (chromatic approach)
    (43, 2.25, 2.625),  # A2 (fifth of D)
    (41, 2.625, 3.0),  # G2 (chromatic approach)
    (38, 3.0, 3.375),  # D2
    (40, 3.375, 3.75),  # F2
    (43, 3.75, 4.125),  # A2
    (41, 4.125, 4.5),  # G2
    (38, 4.5, 4.875),  # D2
    (40, 4.875, 5.25),  # F2
    (43, 5.25, 5.625),  # A2
    (41, 5.625, 6.0)    # G2
]

for note, start, end in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: G7 (G, B, D, F)
# Bar 4: C7 (C, E, G, B)
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    (62, 1.5, 1.875), (67, 1.5, 1.875), (69, 1.5, 1.875), (71, 1.5, 1.875),
    # Bar 3: G7 (G, B, D, F)
    (67, 3.0, 3.375), (71, 3.0, 3.375), (69, 3.0, 3.375), (65, 3.0, 3.375),
    # Bar 4: C7 (C, E, G, B)
    (60, 4.5, 4.875), (64, 4.5, 4.875), (67, 4.5, 4.875), (71, 4.5, 4.875)
]

for note, start, end in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    (67, 1.5, 1.875),  # D4
    (71, 2.25, 2.625),  # F#4
    # Bar 3: Leave it hanging
    (69, 3.0, 3.375),  # A4
    # Bar 4: Come back and finish it
    (67, 4.5, 4.875),  # D4
    (71, 5.25, 5.625)  # F#4
]

for note, start, end in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
