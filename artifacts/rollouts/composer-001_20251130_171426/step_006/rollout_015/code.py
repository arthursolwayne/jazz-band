
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: chromatic approach to Fm
bass_notes = [
    # Bar 2: root (F), chromatic approach (E), root (F)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=63, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),
    # Bar 3: Fm chord tones (F, Ab, C)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=67, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.5625, end=2.75),
    # Bar 4: Fm7 chord with chromatic approach
    pretty_midi.Note(velocity=90, pitch=63, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=64, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=69, start=3.3125, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 1
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.6875),
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.4375),
    # Bar 4: Fm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.9375),
]
piano.notes.extend(piano_notes)

# Sax: Melody — one short motif, make it sing
# Fm: F, Ab, C, Eb
sax_notes = [
    # Bar 2: F (64) on beat 1
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),
    # Bar 3: Ab (67) on beat 2 (leave it hanging)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.4375),
    # Bar 4: C (69) on beat 3, then Eb (62) on beat 4 (finish the motif)
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Bar 3: 1.5 - 3.0s, Bar 4: 3.0 - 4.5s
# But we only need up to 6.0s (4 bars), so we'll extend drum pattern
# Repeat same pattern for bar 3 and 4
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Add the remaining drum notes for bar 4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))
# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
# Hihat on every eighth
for i in range(6):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
    start += 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('waynes_moment.mid')
