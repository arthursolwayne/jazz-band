
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Ride cymbal on every eighth note to set the groove
for i in range(0, 8):
    note = pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=(i + 1) * 0.375)
    drums.notes.append(note)

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([kick1, kick3])

# Snare on 2 and 4
snare2 = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
snare4 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)
drums.notes.extend([snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone (Dante) - Melody
# Dm7: D F A C
# Motif: D (1.5s), F (1.875s), A (2.25s), rest (2.625s)
sax_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax_note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)
sax_note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)
sax.notes.extend([sax_note1, sax_note2, sax_note3])

# Bass (Marcus) - Walking line: D (1.5s), F (1.875s), A (2.25s), C (2.625s), D (3.0s), F (3.375s), A (3.75s), C (4.125s)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=70, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=69, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
# Dm7 on 2 (1.875s), F7 on 4 (2.625s)
# Dm7: D F A C
# F7: F A C Eb
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 12):
    note = pretty_midi.Note(velocity=80, pitch=42, start=(1.5 + i * 0.375), end=(1.5 + (i + 1) * 0.375))
    drums.notes.append(note)

kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25)
drums.notes.extend([kick2, kick3, kick4, kick5])

snare2 = pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25)
snare3 = pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375)
snare4 = pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5)
snare5 = pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625)
drums.notes.extend([snare2, snare3, snare4, snare5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
