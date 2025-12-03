
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
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
]
bass.notes.extend(bass_notes)

# Diane: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
diane_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75),  # C4
]
piano.notes.extend(diane_notes)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick, snare, hihat])

# Dante: saxophone, short motif, starts on beat 2, leaves it hanging
# Dm7 scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=105, pitch=64, start=2.0, end=2.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Diane: open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 -> G7 (G, B, D, F)
diane_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.25),  # F4
]
piano.notes.extend(diane_notes)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick, snare, hihat])

# Dante: saxophone, take the melody, finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=105, pitch=64, start=3.25, end=3.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Diane: open voicings, different chord each bar, resolve on the last
# Bar 4: G7 -> Dm7 (G, B, D, F)
diane_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=4.75),  # F4
]
piano.notes.extend(diane_notes)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick, snare, hihat])

# Dante: saxophone, leave the phrase open, let it hang
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=105, pitch=64, start=4.75, end=5.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
