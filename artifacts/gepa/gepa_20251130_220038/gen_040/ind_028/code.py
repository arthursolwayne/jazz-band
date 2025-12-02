
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
kick_notes = [36, 36, 0, 36, 36, 0, 36, 36]
snare_notes = [0, 38, 38, 0, 0, 38, 38, 0]
hihat_notes = [42] * 8

for i in range(8):
    if kick_notes[i]:
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=i * 0.375, end=(i + 1) * 0.375)
        drums.notes.append(note)
    if snare_notes[i]:
        note = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=i * 0.375, end=(i + 1) * 0.375)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=hihat_notes[i], start=i * 0.375, end=(i + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0)   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25), # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 - G7 - Cm7 - F7 (Dm7 is D F A C)
# First bar: D (start at 1.5), F (start at 1.875), A (start at 2.25), C (start at 2.625)
# Second bar: G (start at 3.0), Bb (start at 3.375), D (start at 3.75), F (start at 4.125)
# Third bar: C (start at 4.5), Eb (start at 4.875), G (start at 5.25), Bb (start at 5.625)

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.125), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.875), # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.625), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=110, pitch=74, start=4.125, end=4.375), # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.125), # Eb
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0)   # Bb
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):  # Bars 2, 3, 4
    start = 1.5 + bar * 1.5
    for i in range(8):
        if kick_notes[i]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=start + i * 0.375, end=start + (i + 1) * 0.375)
            drums.notes.append(note)
        if snare_notes[i]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=start + i * 0.375, end=start + (i + 1) * 0.375)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
