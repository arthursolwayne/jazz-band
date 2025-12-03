
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # Bb2 (chromatic approach)

    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # D3 (octave)
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),  # Eb3 (chromatic approach)

    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # Eb3
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # F3 (fifth)
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),  # E3 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875), # C4

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375), # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375), # Bb3
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Start on D4, then F4, then bend to G4, rest for a beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # G4 (return)
]
for note in sax_notes:
    sax.notes.append(note)

# Add more drum fills in bars 2-4
# Bar 2: Fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=95, pitch=42, start=2.25, end=2.625), # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Fill on beat 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Fill on beat 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=95, pitch=42, start=5.25, end=5.625), # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Add hihat on every eighth in bars 2-4
for bar in range(2, 5):
    for i in range(4):
        start = 1.5 + (bar - 2) * 1.5 + i * 0.375
        end = start + 0.375
        if start < 6.0:
            pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
