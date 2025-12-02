
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab (b3)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # C (5)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),   # Bb (b7)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # Ab (b3)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5),   # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),   # C (5)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Bb (b7)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # Ab (b3)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)    # F (root)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Ab
]
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
]
# Resolution at the end of bar 4
piano_notes_bar4_res = [
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes_bar2)
piano.notes.extend(piano_notes_bar3)
piano.notes.extend(piano_notes_bar4)
piano.notes.extend(piano_notes_bar4_res)

# You: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (MIDI 53), Bb (MIDI 58), D (MIDI 62), F (MIDI 53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=120, pitch=58, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=120, pitch=58, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=6.0)   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)   # Kick on 3
]
drums.notes.extend(drum_notes_bar2)

# Bar 3
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75)  # Kick on 3
]
drums.notes.extend(drum_notes_bar3)

# Bar 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)    # Kick on 3
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
