
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 chromatic approach on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F2 chromatic approach on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # F5
]
# Bar 4: Cm7 (C Eb G Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb4 (octave down)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) to E4 (64) to D4 (62) on beat 1, leave it hanging
# Then come back with E4, F4, D4 on beat 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),   # D4 on 1
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E4 on 2
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D4 on 3
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # E4 on 4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # F4 on 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # D4 on 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: same pattern as before
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Bass: D2 (38) to G2 (43) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Eb2 chromatic approach on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # F2 chromatic approach on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F5
]
# Bar 4: Cm7 (C Eb G Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb4 (octave down)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),   # D4 on 1
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # E4 on 2
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D4 on 3
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # E4 on 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),   # F4 on 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),   # D4 on 4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: same pattern as before
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bass: D2 (38) to G2 (43) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2 chromatic approach on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # F2 chromatic approach on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4 (octave down)
]
piano.notes.extend(piano_notes)

# Sax: End the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),   # D4 on 1
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # E4 on 2
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D4 on 3
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),   # D4 on 4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
