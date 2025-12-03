
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
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

# Bass: walking line in Fm (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=80, pitch=66, start=2.625, end=3.0),   # F2
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),   # G2
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # Ab2
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),   # D2
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.875),   # F2
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # Ab2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
]

# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab4
])

# Bar 4: Dm7 (D, F, Ab, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
])

# Bar 4: E7 (E, G#, B, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # D4
])

# Bar 4: Fm7 (F, Ab, D, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
])

# Bar 4: Bbm7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),  # Ab4
])

# Bar 4: Dm7 (D, F, Ab, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Ab4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C4
])

# Bar 4: E7 (E, G#, B, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # G#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.6875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.6875, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.4375, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.1875),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.9375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.9375, end=4.125), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.6875),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.6875, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.4375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.4375, end=5.625), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.8125), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.8125, end=6.0),   # F4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on beat 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on beat 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on beat 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on beat 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875))
    # Hihat on every eighth
    for i in range(0, 4):
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
