
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum sounds (MIDI note numbers)
KICK = 36
SNARE = 38
HIHAT = 42

# Key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# Scale: F minor (F, Gb, Ab, Bb, B, Db, Eb)

# Time sig: 4/4
# Bar length: 1.5s
# 160 BPM = 60 / 160 * 4 = 1.5s per bar

# BAR 1: Drums only — building tension, a question

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def bar1_drums():
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.125, end=1.5))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.75, end=0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.5, end=1.625))
    
    # Hi-hat on every eighth note
    for i in range(0, 4):
        start = i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

bar1_drums()

# BAR 2: Sax starts the melody, piano enters with open voicings
# Bar 2: Start of the melody — a question, a breath, a plea

# Sax: F (F4), Ab (Ab4), Bb (Bb4), B (B4) — a descending motif with space
# Time in bar: 0.0 to 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75)  # B4
]
sax.notes.extend(sax_notes)

# Piano: Open voicings. Fm7 (F, Ab, Bb, Db), then Ab7 (Ab, C, Eb, Gb)
# Comp on 2 and 4
piano_notes = [
    # Fm7 at 1.5s (start of bar), resolve on 2.0s
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),     # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),     # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),     # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),     # Db4

    # Ab7 at 2.25s (on beat 3), resolve on 2.75s
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.75),   # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.75),   # C5
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.75),   # Eb4
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.75),   # Gb4
]
piano.notes.extend(piano_notes)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Bar 2: F (root), Ab (fifth), G (chromatic approach to Ab), Bb (root)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),   # F2
    pretty_midi.Note(velocity=80, pitch=41, start=1.625, end=1.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=1.875),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.0),   # Bb2
]
bass.notes.extend(bass_notes)

# Drums continue in bar 2
def bar2_drums():
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=2.625, end=2.75))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=2.0, end=2.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=2.75, end=2.875))
    
    # Hi-hat on every eighth note
    for i in range(0, 4):
        start = 1.5 + i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

bar2_drums()

# BAR 3: Sax continues the motif, piano opens further, bass continues the line

# Sax: Echo the first motif with a slight variation
# F4, Ab4, Bb4, B4 again with a little more resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=70, start=3.875, end=4.0)
]
sax.notes.extend(sax_notes)

# Piano: Open voicing, Abm7 (Ab, C, Eb, Gb), then Fm7 again
piano_notes = [
    # Abm7 at 2.75s
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),     # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),     # C5
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),     # Eb4
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),     # Gb4

    # Fm7 at 3.25s
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),     # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),     # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),     # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),     # Db4
]
piano.notes.extend(piano_notes)

# Bass: Walking line in Fm
# Bar 3: Ab (fifth), Bb (root), B (chromatic), C (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=2.875),   # Ab2
    pretty_midi.Note(velocity=80, pitch=37, start=2.875, end=3.0),    # Bb2
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.125),    # B2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=39, start=3.125, end=3.25),   # C2 (chromatic)
]
bass.notes.extend(bass_notes)

# Drums continue in bar 3
def bar3_drums():
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=2.75, end=3.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=3.875, end=4.0))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=3.0, end=3.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=4.0, end=4.125))
    
    # Hi-hat on every eighth note
    for i in range(0, 4):
        start = 2.75 + i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

bar3_drums()

# BAR 4: Full resolution — sax finishes the motif, piano resolves, bass walks to the end

# Sax: Finish the motif with a resolution — F4, Ab4, Bb4, F4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=5.125, end=5.25)
]
sax.notes.extend(sax_notes)

# Piano: Fm7 again, shifted to end of the bar
piano_notes = [
    # Fm7 at 4.0s
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),     # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),     # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),     # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),     # Db4
]
piano.notes.extend(piano_notes)

# Bass: Walking line in Fm
# Bar 4: Db (flatted seventh), F (root), G (chromatic), Ab (fifth)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.0, end=4.125),   # Db2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.25),   # F2
    pretty_midi.Note(velocity=80, pitch=39, start=4.25, end=4.375),   # G2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=41, start=4.375, end=4.5),    # Ab2
]
bass.notes.extend(bass_notes)

# Drums continue in bar 4
def bar4_drums():
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=4.0, end=4.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=5.125, end=5.25))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=4.25, end=4.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=5.25, end=5.375))
    
    # Hi-hat on every eighth note
    for i in range(0, 4):
        start = 4.0 + i * 0.375
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

bar4_drums()

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
