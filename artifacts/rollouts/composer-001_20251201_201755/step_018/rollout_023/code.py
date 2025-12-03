
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.5),  # D2
]
bass.notes.extend(bass_notes)

# Diane on piano (open voicings, different chord each bar, resolve on the last)
piano_notes_bar2 = [
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes_bar2)

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drums_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]
drums.notes.extend(drums_notes_bar2)

# Dante on sax: short motif, start it, leave it hanging, come back and finish it
sax_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A4
]
sax.notes.extend(sax_notes_bar2)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=3.25, end=3.5),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=3.5, end=3.75),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.0),  # D2
]
bass.notes.extend(bass_notes_bar3)

# Diane on piano (open voicings, different chord each bar, resolve on the last)
piano_notes_bar3 = [
    # D7: D, F, A, C#, G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # C#5
]
piano.notes.extend(piano_notes_bar3)

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drums_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drums_notes_bar3)

# Dante on sax: continue the motif, leave it hanging again
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # A4
]
sax.notes.extend(sax_notes_bar3)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.75, end=5.0),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=5.0, end=5.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.5),  # D2
]
bass.notes.extend(bass_notes_bar4)

# Diane on piano (open voicings, different chord each bar, resolve on the last)
piano_notes_bar4 = [
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes_bar4)

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drums_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drums_notes_bar4)

# Dante on sax: finish the motif
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A4
]
sax.notes.extend(sax_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
