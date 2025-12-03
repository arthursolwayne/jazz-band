
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
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=0.0,
        end=1.5
    )
    drums.notes.append(drum_note)

# Bar 2: Start of the melody (1.5 - 3.0s)
# Diane (piano) plays a Dm7 with a chromatic approach
diane_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)
diane_note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
diane_note3 = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0)
diane_note4 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0)
piano.notes.extend([diane_note1, diane_note2, diane_note3, diane_note4])

# Marcus (bass) plays a walking line: D2 -> E2 -> F2 -> G2
marcus_note1 = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=2.0)
marcus_note2 = pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.5)
marcus_note3 = pretty_midi.Note(velocity=100, pitch=41, start=2.5, end=3.0)
marcus_note4 = pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.5)
bass.notes.extend([marcus_note1, marcus_note2, marcus_note3, marcus_note4])

# Little Ray (drums) continues with kick on 1 and 3, snare on 2 and 4
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=1.5,
        end=3.0
    )
    drums.notes.append(drum_note)

# Dante (sax) starts the motif
sax_note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)
sax_note2 = pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5)
sax_note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0)
sax.notes.extend([sax_note1, sax_note2, sax_note3])

# Bar 3: Continue the melody (3.0 - 4.5s)
# Diane (piano) plays an Am7 with a chromatic approach
diane_note5 = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5)
diane_note6 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5)
diane_note7 = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5)
diane_note8 = pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5)
piano.notes.extend([diane_note5, diane_note6, diane_note7, diane_note8])

# Marcus (bass) continues the walking line: A2 -> B2 -> C2 -> D2
marcus_note5 = pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.5)
marcus_note6 = pretty_midi.Note(velocity=100, pitch=47, start=3.5, end=4.0)
marcus_note7 = pretty_midi.Note(velocity=100, pitch=48, start=4.0, end=4.5)
marcus_note8 = pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=5.0)
bass.notes.extend([marcus_note5, marcus_note6, marcus_note7, marcus_note8])

# Little Ray (drums) continues with kick on 1 and 3, snare on 2 and 4
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=3.0,
        end=4.5
    )
    drums.notes.append(drum_note)

# Dante (sax) continues the motif
sax_note4 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5)
sax_note5 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0)
sax_note6 = pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.5)
sax.notes.extend([sax_note4, sax_note5, sax_note6])

# Bar 4: Resolve the motif (4.5 - 6.0s)
# Diane (piano) plays a Dm7 with a chromatic approach
diane_note9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)
diane_note10 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)
diane_note11 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)
diane_note12 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0)
piano.notes.extend([diane_note9, diane_note10, diane_note11, diane_note12])

# Marcus (bass) continues the walking line: D2 -> E2 -> F2 -> G2
marcus_note9 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=5.0)
marcus_note10 = pretty_midi.Note(velocity=100, pitch=40, start=5.0, end=5.5)
marcus_note11 = pretty_midi.Note(velocity=100, pitch=41, start=5.5, end=6.0)
marcus_note12 = pretty_midi.Note(velocity=100, pitch=43, start=6.0, end=6.5)
bass.notes.extend([marcus_note9, marcus_note10, marcus_note11, marcus_note12])

# Little Ray (drums) continues with kick on 1 and 3, snare on 2 and 4
for note in [36, 38, 42]:
    drum_note = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=4.5,
        end=6.0
    )
    drums.notes.append(drum_note)

# Dante (sax) resolves the motif
sax_note7 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0)
sax_note8 = pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.5)
sax_note9 = pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=6.0)
sax.notes.extend([sax_note7, sax_note8, sax_note9])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
