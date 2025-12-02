
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drum_hihat_2 = pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75)
drum_hihat_3 = pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125)
drum_hihat_4 = pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat_2, drum_hihat_3, drum_hihat_4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: Motif - start with Fm7, leave it hanging, come back and resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=110, pitch=63, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
drum_hihat_2 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
drum_hihat_3 = pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
drum_hihat_4 = pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat_2, drum_hihat_3, drum_hihat_4, drum_kick_2])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=110, pitch=63, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
drum_hihat_2 = pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
drum_hihat_3 = pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
drum_hihat_4 = pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_hihat_2, drum_hihat_3, drum_hihat_4, drum_kick_2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
