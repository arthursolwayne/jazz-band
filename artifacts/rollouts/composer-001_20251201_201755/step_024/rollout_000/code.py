
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # F (root) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),
    # C (fifth) with chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),
    # F (root) with chromatic approach from E
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625),
    # C (fifth) with chromatic approach from B
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0)   # E
]
# Bar 3: Bm7 (B, D, F, A)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5)   # A
]
# Bar 4: G7 (G, B, D, F)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=6.0)   # F
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, A, F (melody)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),  # F (delayed resolution)
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.75)   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
# Kick on 1 and 3
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
]
# Snare on 2 and 4
drum_notes_bar3 += [
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0)
]
# Hi-hat on every eighth
drum_notes_bar3 += [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes_bar3)

# Bar 4: Drums
# Kick on 1 and 3
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
]
# Snare on 2 and 4
drum_notes_bar4 += [
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5)
]
# Hi-hat on every eighth
drum_notes_bar4 += [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
