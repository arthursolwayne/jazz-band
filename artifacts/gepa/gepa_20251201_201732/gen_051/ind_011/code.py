
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2-A2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # C3
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # C3
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),   # Bb2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=95, pitch=58, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.875),  # Eb4
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=55, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=95, pitch=50, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=95, pitch=52, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=95, pitch=53, start=2.25, end=2.625),  # F5
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=95, pitch=55, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=95, pitch=58, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=95, pitch=50, start=3.0, end=3.375),  # Bb4
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: F#4 (motif start), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F#4
]
# Bar 3: Repeat motif with slight variation
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F#4
])
# Bar 4: Complete the motif, return to F (F4)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),   # F4
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),   # F4
])
for note in sax_notes:
    sax.notes.append(note)

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    kick_start = start
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = start + 0.75
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2 and 4
    snare_start = start + 0.375
    snare_end = snare_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    snare_start = start + 1.125
    snare_end = snare_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat on every eighth
    for i in range(4):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
