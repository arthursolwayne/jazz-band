
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (MIDI 40) -> C (MIDI 45)
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),
    # Bar 3: G (MIDI 42) -> D (MIDI 47)
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),
    # Bar 4: A (MIDI 44) -> E (MIDI 49)
    pretty_midi.Note(velocity=80, pitch=44, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=3.0),
    # Bar 5: Bb (MIDI 45) -> F (MIDI 50)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),
    # Bar 6: C (MIDI 47) -> G (MIDI 52)
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.0),
    # Bar 7: D (MIDI 49) -> A (MIDI 54)
    pretty_midi.Note(velocity=80, pitch=49, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=54, start=4.25, end=4.5),
    # Bar 8: E (MIDI 51) -> Bb (MIDI 56)
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=56, start=4.75, end=5.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # Eb
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # F
]
# Bar 4: Am7 (A, C, E, G)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
]
# Bar 5: Bb7 (Bb, D, F, Ab)
piano_notes_bar5 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # Ab
]
# Bar 6: C7 (C, E, G, Bb)
piano_notes_bar6 = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0),  # Bb
]
# Bar 7: D7 (D, F#, A, C)
piano_notes_bar7 = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.5),  # C
]
# Bar 8: E7 (E, G#, B, D)
piano_notes_bar8 = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),  # G#
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # D
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4 + piano_notes_bar5 + piano_notes_bar6 + piano_notes_bar7 + piano_notes_bar8)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, D, F (MIDI 57, 60, 64, 57)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=57, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: Kick on 1 and 3, Snare on 2 and 4
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
# Bar 3: Kick on 1 and 3, Snare on 2 and 4
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
]
# Bar 4: Kick on 1 and 3, Snare on 2 and 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=4.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
]
drums.notes.extend(drum_notes_bar2 + drum_notes_bar3 + drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
