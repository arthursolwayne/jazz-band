
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    kick_time = 0.375 * (1 + 2*i)
    snare_time = 0.375 * (2 + 2*i)
    hihat_time = 0.375 * (i*4 + 0)
    for j in range(4):
        hihat_time += 0.375
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=68, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=70, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=73, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=74, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=75, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=76, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=77, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane (Piano): 7th chords, comp on 2 and 4
def add_piano_chord(time, root, seventh):
    root_note = pretty_midi.Note(velocity=100, pitch=root, start=time, end=time + 0.25)
    seventh_note = pretty_midi.Note(velocity=90, pitch=seventh, start=time, end=time + 0.25)
    piano.notes.append(root_note)
    piano.notes.append(seventh_note)

add_piano_chord(1.5, 60, 64)
add_piano_chord(2.25, 62, 66)
add_piano_chord(3.0, 64, 68)
add_piano_chord(3.75, 65, 69)
add_piano_chord(4.5, 67, 71)
add_piano_chord(5.25, 69, 73)

# Dante (Sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4, 8):
    kick_time = 0.375 * (1 + 2*i)
    snare_time = 0.375 * (2 + 2*i)
    hihat_time = 0.375 * (i*4 + 0)
    for j in range(4):
        hihat_time += 0.375
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("waynes_moment.mid")
