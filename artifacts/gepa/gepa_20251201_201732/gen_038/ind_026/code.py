
import pretty_midi

# Initialize the MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note numbers
# Drums: kick=36, snare=38, hihat=42
# Bass: D2=38, G2=43, etc.
# Piano: open voicings in D major
# Sax: motif in D minor, no scales

# Bar 1: Drums only (0.0 to 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.25), (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Start of the melody (1.5s - 3.0s)
# Sax motif: D (62), F (65), Bb (60), D (62)
# Play D-F-Bb-D, leave it hanging on Bb for the first bar
sax_notes = [
    (62, 1.5), (65, 1.5), (60, 1.5), (62, 1.5),
    (60, 3.0)  # leave it hanging on Bb at the end of bar 2
]

for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bass: walking line in D (root, 5th, chromatic approach)
# Bar 2: D2 (38), A2 (45), C#2 (41)
# Bar 3: G2 (43), D2 (38), F#2 (46)
# Bar 4: B2 (49), F#2 (46), D2 (38)
bass_notes = [
    (38, 1.5), (45, 1.75), (41, 2.0),
    (43, 2.25), (38, 2.5), (46, 2.75),
    (49, 3.0), (46, 3.25), (38, 3.5)
]

for note, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: open voicings, different chords each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
# Bar 3: Bm7 (B-D-F#-A)
# Bar 4: G7 (G-B-D-F)
# All on beat 2 and 4
piano_notes = [
    # Bar 2
    (62, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # Dmaj7
    (62, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),
    # Bar 3
    (66, 3.0), (67, 3.0), (71, 3.0), (69, 3.0),  # Bm7
    (66, 3.5), (67, 3.5), (71, 3.5), (69, 3.5),
    # Bar 4
    (67, 4.0), (69, 4.0), (71, 4.0), (74, 4.0),  # G7
    (67, 4.5), (69, 4.5), (71, 4.5), (74, 4.5)
]

for note, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue the pattern for bars 2-4
# Bars 2-4 (1.5s to 6.0s) are 4.5 seconds (3 bars)
# Same pattern repeated for each bar
for bar in range(2, 5):
    time_start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, time_start), (38, time_start + 0.375), (42, time_start), (42, time_start + 0.125),
        (42, time_start + 0.25), (42, time_start + 0.375),
        (36, time_start + 0.75), (38, time_start + 0.875), (42, time_start + 0.75),
        (42, time_start + 0.875),
        (36, time_start + 1.125), (38, time_start + 1.25), (42, time_start + 1.125),
        (42, time_start + 1.25), (42, time_start + 1.375), (42, time_start + 1.5)
    ]
    for note, time in drum_notes:
        note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
