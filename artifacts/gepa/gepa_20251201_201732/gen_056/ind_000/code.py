
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # G#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # B2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: D7sus (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # C#4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Sax: short motif, melodic, clear, questioning
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=2.75, end=3.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # B2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # F#2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # G#2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 3: Dm7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Sax: continuation of motif, resolved
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=4.25, end=4.5),  # G4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F#2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # G#2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 4: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # C#4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Sax: resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=5.75, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
