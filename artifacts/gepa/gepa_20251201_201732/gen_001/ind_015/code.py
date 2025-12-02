
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875), # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in
# Bass: D2 (MIDI 38), walk with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2 on 1
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625), # C2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # F2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: D7 (G, B, D, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # F#4
]

# Bar 3: Bm7b5 (F#, A, D, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # G4
])

# Bar 4: resolve to Gm7 (Bb, D, F, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # G4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif, make it sing
# First note on 1, leave it hanging — then come back
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.875), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25), # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5), # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
