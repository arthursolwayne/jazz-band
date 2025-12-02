
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: F7 on beat 2 again
piano_notes2 = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # D
]
piano.notes.extend(piano_notes2)

# Bar 4: F7 on beat 2 again
piano_notes3 = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),  # D
]
piano.notes.extend(piano_notes3)

# Dante: Sax melody in bar 2, start with a short motif
# Bar 2: Start with motif (F, G, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Continue motif with variation
# Bar 3: Echo the motif, lower by a minor third (D, E, Bb)
sax_notes2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes2)

# Bar 4: Finish the motif, maybe a trill or a resolution
# Bar 4: Move back to F, resolving the phrase
sax_notes3 = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes3)

# Drums: Continue in bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)
hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
drums.notes.extend([kick2, snare2, hihat5, hihat6, hihat7, hihat8])

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat9 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
hihat10 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
hihat11 = pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
hihat12 = pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
drums.notes.extend([kick3, snare3, hihat9, hihat10, hihat11, hihat12])

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat13 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
hihat14 = pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25)
hihat15 = pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
hihat16 = pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
drums.notes.extend([kick4, snare4, hihat13, hihat14, hihat15, hihat16])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
