
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=34, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=36, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=35, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=32, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=37, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=34, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Fm7 on beat 2 of bar 2, Bb7 on beat 2 of bar 3, Eb7 on beat 2 of bar 4
chord_notes = [
    # Bar 2, beat 2 (Fm7) - F, Ab, C, Eb
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=35, start=2.25, end=2.625),
    # Bar 3, beat 2 (Bb7) - Bb, D, F, Ab
    pretty_midi.Note(velocity=100, pitch=32, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=34, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    # Bar 4, beat 2 (Eb7) - Eb, G, Bb, D
    pretty_midi.Note(velocity=100, pitch=35, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=37, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=32, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=34, start=5.25, end=5.625),
]
piano.notes.extend(chord_notes)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25)
drums.notes.extend([kick, snare, hihat])
# Bar 3
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75)
drums.notes.extend([kick, snare, hihat])
# Bar 4
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25)
drums.notes.extend([kick, snare, hihat])

# Dante: saxophone motif
# Bar 2: Start the motif
# F (40), Ab (38), C (37), Bb (32) - 1.5 - 1.875
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=40, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=37, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=32, start=2.625, end=3.0),
    # Bar 3: Complement the motif
    pretty_midi.Note(velocity=110, pitch=34, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=35, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=37, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=40, start=4.125, end=4.5),
    # Bar 4: Return to the motif, finish it
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=37, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=32, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=34, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
