
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

# Fill the bar with hihat and kick/snare on the beat
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=i * 0.375 + 0.375))
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=i * 0.375, end=i * 0.375 + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=i * 0.375 + 0.375, end=i * 0.375 + 0.75))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D minor, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875))  # C5

# Bar 3: G7 (G B D F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # F4

# Bar 4: Cm7 (C Eb G Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # Bb4

# Sax: Motif in D minor, one short phrase, leave it hanging
# Phrase: D (E) F Eb (G) A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.78125))  # E4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.78125, end=1.875))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.0625))  # Eb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625))  # A4

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    if i == 0:
        # Bar 2
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=1.5, end=1.875))  # Kick
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25))  # Snare
    elif i == 1:
        # Bar 3
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=2.25, end=2.625))  # Kick
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=3.0))  # Snare
    elif i == 2:
        # Bar 4
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=3.0, end=3.375))  # Kick
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75))  # Snare
    elif i == 3:
        # Bar 5
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=3.75, end=4.125))  # Kick
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.5))  # Snare

# Add hi-hats on every eighth note in bars 2-4
for i in range(4):
    for j in range(4):
        start = (i + 1) * 1.5 + j * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
