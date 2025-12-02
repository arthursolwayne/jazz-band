
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
drum_snare = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D (D4), F# (F#4), A (A4), C (C5) - simple motif, no scale runs
sax_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax_note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25)
sax_note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)
sax_note4 = pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bass: walking line starting on D (D3), chromatic approach to F#
bass_note1 = pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25)
bass_note3 = pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625)
bass_note4 = pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_note1 = pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875)  # D7: D, F#, A, C
piano_note2 = pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875)
piano_note3 = pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.875)
piano_note4 = pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.875)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, but end on a suspend
sax_note5 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)
sax_note6 = pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75)
sax_note7 = pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125)
sax_note8 = pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Bass: walking line continuing
bass_note5 = pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375)
bass_note6 = pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75)
bass_note7 = pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125)
bass_note8 = pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5)
bass.notes.extend([bass_note5, bass_note6, bass_note7, bass_note8])

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_note5 = pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375)  # D7: D, F#, A, C
piano_note6 = pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375)
piano_note7 = pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.375)
piano_note8 = pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.375)
piano.notes.extend([piano_note5, piano_note6, piano_note7, piano_note8])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat the motif, then resolve
sax_note9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
sax_note10 = pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25)
sax_note11 = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)
sax_note12 = pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0)
sax.notes.extend([sax_note9, sax_note10, sax_note11, sax_note12])

# Bass: walking line continuing
bass_note9 = pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875)
bass_note10 = pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25)
bass_note11 = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625)
bass_note12 = pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0)
bass.notes.extend([bass_note9, bass_note10, bass_note11, bass_note12])

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_note9 = pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875)
piano_note10 = pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.875)
piano_note11 = pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.875)
piano_note12 = pretty_midi.Note(velocity=85, pitch=76, start=4.5, end=4.875)
piano.notes.extend([piano_note9, piano_note10, piano_note11, piano_note12])

# Drums: Bar 3 and 4
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare2 = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125)
drum_hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick2, drum_snare2, drum_hihat2])

drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare3 = pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625)
drum_hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick3, drum_snare3, drum_hihat3])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
