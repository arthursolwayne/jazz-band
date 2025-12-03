
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 - C - G - D (F2, D2, G2, C3)
bass_note1 = pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25)
bass_note3 = pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625)
bass_note4 = pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: F7 - A7 - D7 - F7 (Open voicings, resolve on last)
piano_note1 = pretty_midi.Note(velocity=100, pitch=113, start=1.5, end=2.25)
piano_note2 = pretty_midi.Note(velocity=100, pitch=116, start=1.5, end=2.25)
piano_note3 = pretty_midi.Note(velocity=100, pitch=110, start=1.5, end=2.25)
piano_note4 = pretty_midi.Note(velocity=100, pitch=113, start=2.25, end=3.0)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: Motif - F5 (start), G5 (hold), E5 (end), F5 (resolve)
sax_note1 = pretty_midi.Note(velocity=110, pitch=84, start=1.5, end=1.875)
sax_note2 = pretty_midi.Note(velocity=110, pitch=86, start=1.875, end=2.125)
sax_note3 = pretty_midi.Note(velocity=110, pitch=82, start=2.125, end=2.5)
sax_note4 = pretty_midi.Note(velocity=110, pitch=84, start=2.5, end=3.0)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Drums: Bar 2
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: A2 - E - B - F (A2, E2, B2, F3)
bass_note1 = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375)
bass_note2 = pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75)
bass_note3 = pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125)
bass_note4 = pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: A7 - C7 - F7 - A7 (Open voicings, resolve on last)
piano_note1 = pretty_midi.Note(velocity=100, pitch=116, start=3.0, end=3.75)
piano_note2 = pretty_midi.Note(velocity=100, pitch=111, start=3.0, end=3.75)
piano_note3 = pretty_midi.Note(velocity=100, pitch=113, start=3.0, end=3.75)
piano_note4 = pretty_midi.Note(velocity=100, pitch=116, start=3.75, end=4.5)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: Motif - A5 (start), B5 (hold), G5 (end), A5 (resolve)
sax_note1 = pretty_midi.Note(velocity=110, pitch=87, start=3.0, end=3.375)
sax_note2 = pretty_midi.Note(velocity=110, pitch=89, start=3.375, end=3.625)
sax_note3 = pretty_midi.Note(velocity=110, pitch=84, start=3.625, end=4.0)
sax_note4 = pretty_midi.Note(velocity=110, pitch=87, start=4.0, end=4.5)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Drums: Bar 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C3 - G - D - A (C3, G2, D3, A3)
bass_note1 = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875)
bass_note2 = pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25)
bass_note3 = pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625)
bass_note4 = pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: C7 - E7 - A7 - C7 (Open voicings, resolve on last)
piano_note1 = pretty_midi.Note(velocity=100, pitch=111, start=4.5, end=5.25)
piano_note2 = pretty_midi.Note(velocity=100, pitch=116, start=4.5, end=5.25)
piano_note3 = pretty_midi.Note(velocity=100, pitch=118, start=4.5, end=5.25)
piano_note4 = pretty_midi.Note(velocity=100, pitch=111, start=5.25, end=6.0)
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: Motif - C6 (start), D6 (hold), B5 (end), C6 (resolve)
sax_note1 = pretty_midi.Note(velocity=110, pitch=91, start=4.5, end=4.875)
sax_note2 = pretty_midi.Note(velocity=110, pitch=93, start=4.875, end=5.125)
sax_note3 = pretty_midi.Note(velocity=110, pitch=89, start=5.125, end=5.5)
sax_note4 = pretty_midi.Note(velocity=110, pitch=91, start=5.5, end=6.0)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Drums: Bar 4
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
