
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
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Everyone comes in (1.5 - 3.0s)

# Marcus - Walking bass line in Fm (F, Eb, D, C, Bb, A, G, Ab)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4, Fm7 on 2, Bbm7 on 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # Eb

    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # G
]
piano.notes.extend(piano_notes)

# Dante - Tenor sax starts with a short motif in Fm
# F, Gb, Eb, D (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),   # D
]
sax.notes.extend(sax_notes)

# Bar 3: Continue the energy (3.0 - 4.5s)

# Marcus - Walking bass line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=56, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),   # Eb
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4, Dm7 on 2, Gm7 on 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=56, start=3.375, end=3.75),  # C

    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),   # Eb
]
piano.notes.extend(piano_notes)

# Dante - Continue the motif, expand slightly
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full resolution (4.5 - 6.0s)

# Marcus - Walking bass line ends
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4, Cm7 on 2, Fm7 on 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # Ab

    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),   # Eb
]
piano.notes.extend(piano_notes)

# Dante - End with a resolution, Fm chord
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),   # Eb
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
