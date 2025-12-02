
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # Snare on 4 (out of bar 1)
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: start of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F#4
]

sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.25),  # C3
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5),  # D3
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # F#7
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # F#7
]

piano.notes.extend(piano_notes)

# Drums: continue (bars 2-4)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=start + i * 0.375, end=start + 1.5))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start + 1.5, end=start + 1.875))

# Bar 3: Sax continues motif (3.0 - 4.5s)
# Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # C#5
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # C#5
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D4
]

sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.25),  # Eb3
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),  # E3
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.75),  # D3
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0),  # C3
    pretty_midi.Note(velocity=80, pitch=39, start=4.0, end=4.25),  # B2
]

bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # F#7
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),  # F#7
]

piano.notes.extend(piano_notes)

# Bar 4: End with a question (4.5 - 6.0s)
# Sax: resolve the motif, but leave it open
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # C#5
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F#4
]

sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=80, pitch=41, start=4.75, end=5.0),  # Eb3
    pretty_midi.Note(velocity=80, pitch=39, start=5.0, end=5.25),  # C3
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.5),  # D3
    pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.75),  # Eb3
    pretty_midi.Note(velocity=80, pitch=39, start=5.75, end=6.0),  # C3
]

bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # F#7
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),  # F#7
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
