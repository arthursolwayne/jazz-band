
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

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)

kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
hihat5 = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)
hihat6 = pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2, snare2, hihat5, hihat6, hihat7, hihat8])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75), # Db
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 on bar 2, Bb7 on bar 3, Eb7 on bar 4
chord1 = [42, 46, 47, 50]  # F7
chord2 = [45, 49, 50, 53]  # Bb7
chord3 = [40, 43, 44, 47]  # Eb7

# Comp on 2 and 4
piano_notes = []
for note in chord1:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.875, end=2.25))
for note in chord2:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.375, end=3.75))
for note in chord3:
    piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=5.25, end=5.625))

piano.notes.extend(piano_notes)

# Sax: Motif in Fm, start it, leave it hanging, come back and finish it
# Motif: F, Ab, Bb, D (Fm7)
note1 = pretty_midi.Note(velocity=110, pitch=42, start=1.5, end=1.875)
note2 = pretty_midi.Note(velocity=110, pitch=40, start=1.875, end=2.25)
note3 = pretty_midi.Note(velocity=110, pitch=41, start=2.25, end=2.625)
note4 = pretty_midi.Note(velocity=110, pitch=46, start=2.625, end=3.0)  # D (Bb7)
note5 = pretty_midi.Note(velocity=110, pitch=42, start=3.0, end=3.375)
note6 = pretty_midi.Note(velocity=110, pitch=40, start=3.375, end=3.75)
note7 = pretty_midi.Note(velocity=110, pitch=41, start=3.75, end=4.125)
note8 = pretty_midi.Note(velocity=110, pitch=46, start=4.125, end=4.5)
note9 = pretty_midi.Note(velocity=110, pitch=42, start=4.5, end=4.875)
note10 = pretty_midi.Note(velocity=110, pitch=40, start=4.875, end=5.25)
note11 = pretty_midi.Note(velocity=110, pitch=41, start=5.25, end=5.625)
note12 = pretty_midi.Note(velocity=110, pitch=46, start=5.625, end=6.0)

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8, note9, note10, note11, note12])

# Drums for bars 2-4
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
hihat9 = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)
hihat10 = pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
hihat11 = pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125)
hihat12 = pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
hihat13 = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875)
hihat14 = pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
hihat15 = pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
hihat16 = pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)

drums.notes.extend([kick3, snare3, hihat9, hihat10, hihat11, hihat12, kick4, snare4, hihat13, hihat14, hihat15, hihat16, kick5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
