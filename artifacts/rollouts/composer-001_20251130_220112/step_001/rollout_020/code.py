
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

# Bar 2: Everybody in (1.5 - 3.0s)
# Sax melody: D, F#, A, B
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: walking line in D (D, E, F#, G, A, B, C#, D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 on beat 2
chord1 = pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0)
chord2 = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0)
chord3 = pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0)
chord4 = pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0)
piano.notes.extend([chord1, chord2, chord3, chord4])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, then resolve on D
note5 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)
note6 = pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5)
note7 = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)
note8 = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0)
sax.notes.extend([note5, note6, note7, note8])

# Bass: D7 chord, walking line
bass_notes2 = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=66, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0)
]
bass.notes.extend(bass_notes2)

# Piano: D7 on 2 and 4
chord5 = pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5)
chord6 = pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5)
chord7 = pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5)
chord8 = pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5)
chord9 = pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25)
chord10 = pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25)
chord11 = pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25)
chord12 = pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25)
piano.notes.extend([chord5, chord6, chord7, chord8, chord9, chord10, chord11, chord12])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End on D
note9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)
sax.notes.append(note9)

# Bass: D7 chord, walking line
bass_notes3 = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=66, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=72, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=62, start=6.25, end=6.5)
]
bass.notes.extend(bass_notes3)

# Piano: D7 on 2 and 4
chord13 = pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0)
chord14 = pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0)
chord15 = pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0)
chord16 = pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0)
chord17 = pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75)
chord18 = pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75)
chord19 = pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75)
chord20 = pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75)
piano.notes.extend([chord13, chord14, chord15, chord16, chord17, chord18, chord19, chord20])

# Drums: Bar 3 and 4
# Bar 3
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick2, snare2, hihat2])

# Bar 4
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick3, snare3, hihat3])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
