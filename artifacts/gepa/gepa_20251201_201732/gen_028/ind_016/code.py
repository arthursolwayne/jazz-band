
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line (F2, G2, A2, Bb2, C3, D3, E3, F3)
bass_notes = [
    # Bar 2: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    # Bar 2: G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),
    # Bar 3: A2 (root + 2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),
    # Bar 3: Bb2 (fifth + 2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),
    # Bar 4: C3 (root + 4) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    # Bar 4: D3 (fifth + 4) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    # Bar 4: E3 (root + 6) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),
    # Bar 4: F3 (root + 7) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
]

# Bar 3: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),
])

# Bar 4: Bbmaj7 (Bb, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Bb (58), F (53), D (62) — phrase it over 4 bars with resolution in bar 4
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25),
    # Bar 3: Continue, leave it hanging
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),
    # Bar 4: Finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5))
    # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
