
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

# Drums in Bar 1 (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drum_hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
drum_hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
drum_hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat2, drum_hihat3, drum_hihat4])

# Bar 2: Full band (1.5 - 3.0s)
# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> Gm7 -> Cm7 -> F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),   # E4

    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),   # G3
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),   # Bb3
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),   # C3
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),   # D3

    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),   # C3
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),   # G3
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),   # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # C2

    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),   # Bb4
]
piano.notes.extend(piano_notes)

# Drums in Bar 2 (1.5 - 3.0s)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
drum_hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
drum_hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625)
drum_hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
drums.notes.extend([drum_kick2, drum_snare2, drum_hihat5, drum_hihat6, drum_hihat7, drum_hihat8])

# Sax: Melodic idea in Dm, short and haunting
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # E4
]
sax.notes.extend(sax_notes)

# Bar 3: Full band (3.0 - 4.5s)
# Bass: walking line in Dm
bass_notes2 = [
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # Eb2
]
bass.notes.extend(bass_notes2)

# Piano: Gm7 -> Cm7 -> F7 -> Dm7
piano_notes2 = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),   # G3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),   # Bb3
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),   # C3
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),   # D3

    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),   # G4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),   # E4

    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),   # C3
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),   # G3
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),   # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),   # C2

    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),   # Bb4
]
piano.notes.extend(piano_notes2)

# Drums in Bar 3 (3.0 - 4.5s)
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat9 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drum_hihat10 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
drum_hihat11 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
drum_hihat12 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
drums.notes.extend([drum_kick3, drum_snare3, drum_hihat9, drum_hihat10, drum_hihat11, drum_hihat12])

# Sax: Repeat and resolve
sax_notes2 = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # E4
]
sax.notes.extend(sax_notes2)

# Bar 4: Full band (4.5 - 6.0s)
# Bass: walking line in Dm
bass_notes3 = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes3)

# Piano: Dm7 -> Gm7 -> Cm7 -> F7
piano_notes3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),   # G4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),   # E4

    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),   # G3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),   # Bb3
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),   # C3
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),   # D3

    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),   # C3
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),   # G3
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),   # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),   # C2

    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),   # Bb4
]
piano.notes.extend(piano_notes3)

# Drums in Bar 4 (4.5 - 6.0s)
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat13 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drum_hihat14 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
drum_hihat15 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
drum_hihat16 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
drums.notes.extend([drum_kick4, drum_snare4, drum_hihat13, drum_hihat14, drum_hihat15, drum_hihat16])

# Sax: Repeat and resolve
sax_notes3 = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # E4
]
sax.notes.extend(sax_notes3)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
