
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0), # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25), # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: C7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0), # C4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0), # C5
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75), # Bb5
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Sax melody (start on 1.5s)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drum_notes(start_time, kick=True, snare=True, hihat=True):
    if kick:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    if snare:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75))
    if hihat:
        for i in range(4):
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.125))

# Bar 2
add_drum_notes(1.5, kick=True, snare=True, hihat=True)
# Bar 3
add_drum_notes(3.0, kick=True, snare=True, hihat=True)
# Bar 4
add_drum_notes(4.5, kick=True, snare=True, hihat=True)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
