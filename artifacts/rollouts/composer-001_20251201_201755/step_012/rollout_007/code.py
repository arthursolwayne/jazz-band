
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
drums.notes.append(drum_kick)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drums.notes.append(drum_snare)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.append(drum_hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
sax.notes.append(sax_note1)
sax_note2 = pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625)
sax.notes.append(sax_note2)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_note1 = pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875)
bass.notes.append(bass_note1)
bass_note2 = pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625)
bass.notes.append(bass_note2)

# Piano: Open voicing, Dm7 (D-F-A-C)
piano_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)
piano.notes.append(piano_note1)
piano_note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0)
piano.notes.append(piano_note2)
piano_note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
piano.notes.append(piano_note3)
piano_note4 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0)
piano.notes.append(piano_note4)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drums.notes.append(drum_kick)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drums.notes.append(drum_snare)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
drums.notes.append(drum_hihat)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif, leave it hanging
sax_note3 = pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375)
sax.notes.append(sax_note3)
sax_note4 = pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.125)
sax.notes.append(sax_note4)

# Bass: Walking line
bass_note3 = pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375)
bass.notes.append(bass_note3)
bass_note4 = pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125)
bass.notes.append(bass_note4)

# Piano: G7 (G-B-D-F)
piano_note5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
piano.notes.append(piano_note5)
piano_note6 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5)
piano.notes.append(piano_note6)
piano_note7 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5)
piano.notes.append(piano_note7)
piano_note8 = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5)
piano.notes.append(piano_note8)

# Drums
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drums.notes.append(drum_kick)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drums.notes.append(drum_snare)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)
drums.notes.append(drum_hihat)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_note5 = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875)
sax.notes.append(sax_note5)
sax_note6 = pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625)
sax.notes.append(sax_note6)

# Bass: Walking line
bass_note5 = pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875)
bass.notes.append(bass_note5)
bass_note6 = pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625)
bass.notes.append(bass_note6)

# Piano: Dm7 with resolution
piano_note9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)
piano.notes.append(piano_note9)
piano_note10 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0)
piano.notes.append(piano_note10)
piano_note11 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)
piano.notes.append(piano_note11)
piano_note12 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)
piano.notes.append(piano_note12)

# Drums
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(drum_kick)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drums.notes.append(drum_snare)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)
drums.notes.append(drum_hihat)

# Save the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
