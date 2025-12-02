
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

bar_length = 1.5
for beat in [0, 2]:  # Beats 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.1)
    drums.notes.append(kick)
for beat in [1, 3]:  # Beats 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.1)
    drums.notes.append(snare)
for i in range(8):  # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=i * 0.375 + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=1.875 + 0.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.25 + 0.375),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=2.625 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.999, end=2.999 + 0.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.375 + 0.375),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.75 + 0.375),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.125 + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.5 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=4.875 + 0.375),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=5.25, end=5.25 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=79, start=5.625, end=5.625 + 0.375),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
def add_piano_note(pitch, time):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Bar 2
add_piano_note(67, 1.5)  # D7: D, F#, A, C
add_piano_note(71, 1.5)
add_piano_note(74, 1.5)
add_piano_note(76, 1.5)

# Bar 3
add_piano_note(67, 3.0)  # D7 again
add_piano_note(71, 3.0)
add_piano_note(74, 3.0)
add_piano_note(76, 3.0)

# Bar 4
add_piano_note(67, 4.5)  # D7 once more
add_piano_note(71, 4.5)
add_piano_note(74, 4.5)
add_piano_note(76, 4.5)

# Sax: Your moment. One short motif, make it sing
# Start on D (62), Bb (60), C (60), D (62) – a simple but emotionally charged motif

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.125),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.625 + 0.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.75 + 0.125),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=1.875 + 0.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.0 + 0.125),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.125, end=2.125 + 0.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.25 + 0.125),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.375, end=2.375 + 0.125),  # Bb
]

sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    for beat in [0, 2]:  # Beats 1 and 3
        kick = pretty_midi.Note(velocity=100, pitch=36, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat * 0.375) + 0.1)
        drums.notes.append(kick)
    for beat in [1, 3]:  # Beats 2 and 4
        snare = pretty_midi.Note(velocity=110, pitch=38, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat * 0.375) + 0.1)
        drums.notes.append(snare)
    for i in range(8):  # Hihat on every eighth
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=(bar * 1.5) + (i * 0.375), end=(bar * 1.5) + (i * 0.375) + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
