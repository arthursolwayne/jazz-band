
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
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Repeat for the next three beats in the bar
for i in range(1, 4):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=i * 0.75, end=i * 0.75 + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=i * 0.75 + 0.375, end=i * 0.75 + 0.75)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * 0.75, end=i * 0.75 + 0.375)
    drums.notes.extend([kick, snare, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Fm7 = F, Ab, Bb, D
# Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, D
# Amaj7 = A, C#, E, G#
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),   # D
]
piano.notes.extend(piano_notes)

# Dante: Melody - one short motif, make it sing
# Fm - start on Ab (Bb is the 3rd), use chromatic passing tones
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),   # F
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 5):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=i * 1.5, end=i * 1.5 + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=i * 1.5 + 0.75, end=i * 1.5 + 1.125)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5, end=i * 1.5 + 1.5)
    drums.notes.extend([kick, snare, hihat])

# Add fills on 2 and 4 with ghost notes
for i in range(2, 5):
    ghost1 = pretty_midi.Note(velocity=70, pitch=36, start=i * 1.5 + 0.375, end=i * 1.5 + 0.5)
    ghost2 = pretty_midi.Note(velocity=70, pitch=38, start=i * 1.5 + 1.125, end=i * 1.5 + 1.25)
    drums.notes.extend([ghost1, ghost2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
