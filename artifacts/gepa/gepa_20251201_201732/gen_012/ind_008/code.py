
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
    # Kick on 1 and 3 (0.0, 0.75, 1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.875),
    # Snare on 2 and 4 (0.375, 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.125, end=1.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line D2-G2 with chromatic approaches
bass_notes = [
    # D2 (D2 = MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),
    # F (chromatic approach up)
    pretty_midi.Note(velocity=80, pitch=41, start=1.625, end=1.75),
    # G2 (G2 = MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=1.875),
    # F (chromatic approach down)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),
    # D2
    pretty_midi.Note(velocity=80, pitch=38, start=2.0, end=2.125),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.125, end=2.25),
    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.375),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.375, end=2.5),
    # D2
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.625),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=2.75),
    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=2.875),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E♭)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),  # E♭
]
# Bar 3: B♭7 (B♭ D F A♭)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # B♭
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),  # A♭
])
# Bar 4: C7 (C E G B♭)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),  # B♭
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: motif starts (F, B♭, C)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # C
    # Leave it hanging (no note in the next 0.625s)
    # Bar 3: return with a resolution (F)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),  # F
    # Bar 4: continue with a line (B♭, C, F)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3 (3.0, 3.75)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.875),
    # Snare on 2 and 4 (3.375, 4.125)
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3 (4.5, 5.25)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.375),
    # Snare on 2 and 4 (4.875, 5.625)
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line D2-G2 with chromatic approaches
bass_notes = [
    # D2 (D2 = MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.125),
    # F (chromatic approach up)
    pretty_midi.Note(velocity=80, pitch=41, start=3.125, end=3.25),
    # G2 (G2 = MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.375),
    # F (chromatic approach down)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.5),
    # D2
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.625),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.625, end=3.75),
    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=3.875),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.875, end=4.0),
    # D2
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.125),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.25),
    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.375),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.375, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: B♭7 (B♭ D F A♭)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # B♭
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # A♭
]
piano.notes.extend(piano_notes)

# Sax: continue with the motif
sax_notes = [
    # Bar 3: continue with a line (F, B♭, C)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # C
    # Bar 4: continue with a line (F, B♭, C, F)
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line D2-G2 with chromatic approaches
bass_notes = [
    # D2 (D2 = MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.625),
    # F (chromatic approach up)
    pretty_midi.Note(velocity=80, pitch=41, start=4.625, end=4.75),
    # G2 (G2 = MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=4.875),
    # F (chromatic approach down)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.0),
    # D2
    pretty_midi.Note(velocity=80, pitch=38, start=5.0, end=5.125),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.125, end=5.25),
    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.375),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.375, end=5.5),
    # D2
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.625),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=5.75),
    # G2
    pretty_midi.Note(velocity=80, pitch=43, start=5.75, end=5.875),
    # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.875, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G B♭)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # B♭
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    # Bar 4: continue with a line (B♭, C, F)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_moment.mid")
