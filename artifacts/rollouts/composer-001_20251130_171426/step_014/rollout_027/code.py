
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
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=49, start=2.0, end=2.25),  # D#
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=52, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.25),  # G#
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=56, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # C#
    pretty_midi.Note(velocity=100, pitch=56, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.25),  # D#
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(8):
    time = 1.5 + beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start of motif
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75)  # Bb
sax.notes.append(note)

# Bar 3: Leave it hanging
note = pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75)  # Bb
sax.notes.append(note)

# Bar 4: Come back and finish it
note = pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75)  # Bb
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25)  # D
sax.notes.append(note)

# Add the rest of the motif
note = pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75)  # C
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0)  # Bb
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne.mid")
