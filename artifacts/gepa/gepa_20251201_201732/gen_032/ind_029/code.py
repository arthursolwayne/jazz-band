
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_kick_1 = pretty_midi.Note(
    velocity=100, pitch=36, start=0.0, end=0.375
)
drum_snare_1 = pretty_midi.Note(
    velocity=100, pitch=38, start=0.75, end=1.125
)
drum_hihat_1 = pretty_midi.Note(
    velocity=90, pitch=42, start=0.0, end=1.5
)
drums.notes.extend([drum_kick_1, drum_snare_1, drum_hihat_1])

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43), root-fifth with chromatic approaches
bass_note_1 = pretty_midi.Note(
    velocity=90, pitch=38, start=1.5, end=1.875
)
bass_note_2 = pretty_midi.Note(
    velocity=90, pitch=41, start=1.875, end=2.25
)
bass_note_3 = pretty_midi.Note(
    velocity=90, pitch=43, start=2.25, end=2.625
)
bass_note_4 = pretty_midi.Note(
    velocity=90, pitch=40, start=2.625, end=3.0
)
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D F# A C#)
piano_note_1 = pretty_midi.Note(
    velocity=100, pitch=62, start=1.5, end=3.0
)
piano_note_2 = pretty_midi.Note(
    velocity=100, pitch=67, start=1.5, end=3.0
)
piano_note_3 = pretty_midi.Note(
    velocity=100, pitch=72, start=1.5, end=3.0
)
piano_note_4 = pretty_midi.Note(
    velocity=100, pitch=74, start=1.5, end=3.0
)
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4])

# Sax: motif, concise and emotional - start on F# (MIDI 67), G# (MIDI 69), then leave it hanging
sax_note_1 = pretty_midi.Note(
    velocity=110, pitch=67, start=1.5, end=1.875
)
sax_note_2 = pretty_midi.Note(
    velocity=110, pitch=69, start=1.875, end=2.25
)
sax.notes.extend([sax_note_1, sax_note_2])

# Bar 3: Full ensemble (3.0 - 4.5s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43), root-fifth with chromatic approaches
bass_note_5 = pretty_midi.Note(
    velocity=90, pitch=38, start=3.0, end=3.375
)
bass_note_6 = pretty_midi.Note(
    velocity=90, pitch=41, start=3.375, end=3.75
)
bass_note_7 = pretty_midi.Note(
    velocity=90, pitch=43, start=3.75, end=4.125
)
bass_note_8 = pretty_midi.Note(
    velocity=90, pitch=40, start=4.125, end=4.5
)
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano: next chord, Bm7 (B D F# A)
piano_note_5 = pretty_midi.Note(
    velocity=100, pitch=71, start=3.0, end=4.5
)
piano_note_6 = pretty_midi.Note(
    velocity=100, pitch=74, start=3.0, end=4.5
)
piano_note_7 = pretty_midi.Note(
    velocity=100, pitch=76, start=3.0, end=4.5
)
piano_note_8 = pretty_midi.Note(
    velocity=100, pitch=79, start=3.0, end=4.5
)
piano.notes.extend([piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick_2 = pretty_midi.Note(
    velocity=100, pitch=36, start=3.0, end=3.375
)
drum_snare_2 = pretty_midi.Note(
    velocity=100, pitch=38, start=3.75, end=4.125
)
drum_hihat_2 = pretty_midi.Note(
    velocity=90, pitch=42, start=3.0, end=4.5
)
drums.notes.extend([drum_kick_2, drum_snare_2, drum_hihat_2])

# Bar 4: Full ensemble (4.5 - 6.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43), root-fifth with chromatic approaches
bass_note_9 = pretty_midi.Note(
    velocity=90, pitch=38, start=4.5, end=4.875
)
bass_note_10 = pretty_midi.Note(
    velocity=90, pitch=41, start=4.875, end=5.25
)
bass_note_11 = pretty_midi.Note(
    velocity=90, pitch=43, start=5.25, end=5.625
)
bass_note_12 = pretty_midi.Note(
    velocity=90, pitch=40, start=5.625, end=6.0
)
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: next chord, G7 (G B D F)
piano_note_9 = pretty_midi.Note(
    velocity=100, pitch=67, start=4.5, end=6.0
)
piano_note_10 = pretty_midi.Note(
    velocity=100, pitch=71, start=4.5, end=6.0
)
piano_note_11 = pretty_midi.Note(
    velocity=100, pitch=72, start=4.5, end=6.0
)
piano_note_12 = pretty_midi.Note(
    velocity=100, pitch=74, start=4.5, end=6.0
)
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick_3 = pretty_midi.Note(
    velocity=100, pitch=36, start=4.5, end=4.875
)
drum_snare_3 = pretty_midi.Note(
    velocity=100, pitch=38, start=5.25, end=5.625
)
drum_hihat_3 = pretty_midi.Note(
    velocity=90, pitch=42, start=4.5, end=6.0
)
drums.notes.extend([drum_kick_3, drum_snare_3, drum_hihat_3])

# Sax: return to motif, finish it
sax_note_3 = pretty_midi.Note(
    velocity=110, pitch=69, start=5.25, end=5.625
)
sax_note_4 = pretty_midi.Note(
    velocity=110, pitch=67, start=5.625, end=6.0
)
sax.notes.extend([sax_note_3, sax_note_4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
