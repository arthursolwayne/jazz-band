
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
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)

drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D, F, A, C
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - Eb - D - Bb (Dm sound, with tension)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=59, start=2.625, end=3.0),   # Bb
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)

drums.notes.extend([kick2, snare2, hihat5, hihat6, hihat7, hihat8])

# Bass: Walking line in Dm, chromatic approaches
bass_notes2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
]

bass.notes.extend(bass_notes2)

# Piano: 7th chords on 2 and 4
piano_notes2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C
]

piano.notes.extend(piano_notes2)

# Sax: Continue the motif, resolve it
sax_notes2 = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),   # D
]

sax.notes.extend(sax_notes2)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)

drums.notes.extend([kick3, snare3, hihat9, hihat10, hihat11, hihat12])

# Bass: Walking line in Dm, chromatic approaches
bass_notes3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb
]

bass.notes.extend(bass_notes3)

# Piano: 7th chords on 2 and 4
piano_notes3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # C
]

piano.notes.extend(piano_notes3)

# Sax: End on a strong note
sax_notes3 = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),   # D
]

sax.notes.extend(sax_notes3)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
