
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drum_hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
drum_hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
drum_hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_snare_1, drum_hihat_1, drum_hihat_2, drum_hihat_3, drum_hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Melody
note_1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75)  # F4
note_2 = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0)  # G4
note_3 = pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25)  # A4
note_4 = pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5)  # B4
note_5 = pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75)  # A4
note_6 = pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0)  # G4
note_7 = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25)  # F4
note_8 = pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5)  # D4
note_9 = pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75)  # E4
note_10 = pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0)  # F#4
note_11 = pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25)  # E4
note_12 = pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5)  # D4
note_13 = pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75)  # C4
note_14 = pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0)  # D4
note_15 = pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25)  # E4
note_16 = pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5)  # F4
note_17 = pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75)  # G4
note_18 = pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0)  # A4
sax.notes.extend([note_1, note_2, note_3, note_4, note_5, note_6, note_7, note_8, note_9, note_10, note_11, note_12, note_13, note_14, note_15, note_16, note_17, note_18])

# Bass: Walking line
bass_note_1 = pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75)  # F3
bass_note_2 = pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0)  # G3
bass_note_3 = pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.25)  # A3
bass_note_4 = pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.5)  # B3
bass_note_5 = pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75)  # A3
bass_note_6 = pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0)  # G3
bass_note_7 = pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25)  # F3
bass_note_8 = pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5)  # D3
bass_note_9 = pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75)  # E3
bass_note_10 = pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0)  # F#3
bass_note_11 = pretty_midi.Note(velocity=80, pitch=53, start=4.0, end=4.25)  # E3
bass_note_12 = pretty_midi.Note(velocity=80, pitch=51, start=4.25, end=4.5)  # D3
bass_note_13 = pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.75)  # C3
bass_note_14 = pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0)  # D3
bass_note_15 = pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25)  # E3
bass_note_16 = pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5)  # F3
bass_note_17 = pretty_midi.Note(velocity=80, pitch=55, start=5.5, end=5.75)  # G3
bass_note_18 = pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0)  # A3
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4, bass_note_5, bass_note_6, bass_note_7, bass_note_8, bass_note_9, bass_note_10, bass_note_11, bass_note_12, bass_note_13, bass_note_14, bass_note_15, bass_note_16, bass_note_17, bass_note_18])

# Piano: 7th chords, comp on 2 and 4
piano_note_1 = pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0)  # D4
piano_note_2 = pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0)  # E4
piano_note_3 = pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0)  # G4
piano_note_4 = pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0)  # B4
piano_note_5 = pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25)  # D4
piano_note_6 = pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25)  # E4
piano_note_7 = pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25)  # G4
piano_note_8 = pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25)  # B4
piano_note_9 = pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75)  # D4
piano_note_10 = pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75)  # E4
piano_note_11 = pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75)  # G4
piano_note_12 = pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75)  # B4
piano_note_13 = pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25)  # D4
piano_note_14 = pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25)  # E4
piano_note_15 = pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25)  # G4
piano_note_16 = pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25)  # B4
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4, piano_note_5, piano_note_6, piano_note_7, piano_note_8, piano_note_9, piano_note_10, piano_note_11, piano_note_12, piano_note_13, piano_note_14, piano_note_15, piano_note_16])

# Drums: Continue after bar 1
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.75)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat_1, hihat_2, hihat_3, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
